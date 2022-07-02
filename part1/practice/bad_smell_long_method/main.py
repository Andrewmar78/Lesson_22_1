# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля
from typing import Optional

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list() -> Optional[list or None]:
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv) -> list:
    # Чтение данных из строки
    data = [line.split(";") for line in csv.split('\n')]
    return data


def _sort(data) -> list:
    # Сортировка по возрасту по возрастанию
    def age(people):
        return people[1]
    data.sort(key=age)
    return data


def _filter(data_sorted) -> Optional[list or None]:
    data_filtered = [item for item in data_sorted if int(item[1]) > 10]
    return data_filtered


if __name__ == '__main__':
    print(get_users_list())
