documents = [
    {
        "name": "Python基础",
        "type": "PDF",
        "pages": 220,
        "course": "Python程序设计",
        "is_finished": True,
    },
    {
        "name": "机器学习入门",
        "type": "视频",
        "pages": 80,
        "course": "机器学习",
        "is_finished": False,
    },
    {
        "name": "高等数学复习",
        "type": "笔记",
        "pages": 120,
        "course": "高等数学",
        "is_finished": True,
    },
]


def count_finished_documents(documents):
    finished_count = 0

    for document in documents:
        if document["is_finished"]:
            finished_count += 1

    return finished_count


def calculate_total_pages(documents):
    total_pages = 0

    for document in documents:
        total_pages += document["pages"]

    return total_pages


def find_largest_document(documents):
    if len(documents) == 0:
        return None

    largest_document = documents[0]

    for document in documents:
        if document["pages"] > largest_document["pages"]:
            largest_document = document

    return largest_document


def show_statistics(documents):
    document_count = len(documents)
    finished_count = count_finished_documents(documents)
    unfinished_count = document_count - finished_count
    total_pages = calculate_total_pages(documents)
    largest_document = find_largest_document(documents)

    print("===== 学习资料统计 =====")
    print(f"资料总数：{document_count}")
    print(f"已完成数量：{finished_count}")
    print(f"未完成数量：{unfinished_count}")
    print(f"资料总页数：{total_pages}")

    if largest_document is not None:
        print(f"页数最多的资料：{largest_document['name']}")
        print(f"最多页数：{largest_document['pages']}")


show_statistics(documents)