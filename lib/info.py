# info.py处理以下信息
# title, create, modified


def generate_title(title):
    assert isinstance(title, str), "Title must be strings!"

    return title


def generate_time(year, month, day):
    return "{}.{:0>2}.{:0>2}".format(
        year,
        month,
        day
    )
