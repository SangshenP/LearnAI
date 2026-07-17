import json


def create_document():
    document_name = input("请输入资料名称：")
    document_type = input("请输入资料类型：")
    page_count = int(input("请输入资料页数："))
    course_name = input("请输入所属课程：")
    author = input("请输入资料作者：")

    document = {
        "name": document_name,
        "type": document_type,
        "pages": page_count,
        "course": course_name,
        "author": author,
        "is_finished": False,
    }

    return document


def show_documents(documents):
    if len(documents) == 0:
        print("当前没有学习资料。")
        return

    print("\n===== 所有资料 =====")
    print(f"资料总数：{len(documents)}")

    for index, document in enumerate(documents, start=1):
        status = "已完成" if document["is_finished"] else "未完成"

        print(f"\n第 {index} 份资料")
        print(f"资料名称：{document['name']}")
        print(f"资料类型：{document['type']}")
        print(f"资料页数：{document['pages']}")
        print(f"所属课程：{document['course']}")
        print(f"资料作者：{document['author']}")
        print(f"学习状态：{status}")


def find_document(documents, target_name):
    for document in documents:
        if document["name"] == target_name:
            return document

    return None


def mark_document_finished(documents, target_name):
    document = find_document(documents, target_name)

    if document is None:
        return False

    document["is_finished"] = True
    return True


def save_documents(documents):
    with open("documents.json", "w", encoding="utf-8") as file:
        json.dump(documents, file, ensure_ascii=False, indent=4)


def load_documents():
    try:
        with open("documents.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


documents = load_documents()

while True:
    print("\n===== 学习资料管理器 =====")
    print("1. 添加资料")
    print("2. 查看所有资料")
    print("3. 查找资料")
    print("4. 标记为已完成")
    print("0. 退出程序")

    choice = input("请选择功能：")

    if choice == "1":
        document = create_document()
        documents.append(document)
        save_documents(documents)
        print("资料添加成功。")

    elif choice == "2":
        show_documents(documents)

    elif choice == "3":
        search_name = input("请输入要查找的资料名称：")
        result = find_document(documents, search_name)

        if result is None:
            print("没有找到这份资料。")
        else:
            status = "已完成" if result["is_finished"] else "未完成"

            print("\n===== 查找结果 =====")
            print(f"资料名称：{result['name']}")
            print(f"资料类型：{result['type']}")
            print(f"资料页数：{result['pages']}")
            print(f"所属课程：{result['course']}")
            print(f"资料作者：{result['author']}")
            print(f"学习状态：{status}")

    elif choice == "4":
        finish_name = input("请输入已经学完的资料名称：")
        is_success = mark_document_finished(documents, finish_name)

        if is_success:
            save_documents(documents)
            print("学习状态修改成功。")
        else:
            print("没有找到这份资料。")

    elif choice == "0":
        print("程序已退出。")
        break

    else:
        print("输入无效，请重新选择。")