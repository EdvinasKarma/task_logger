from datetime import datetime

from task_logger import TaskLogger


def get_empty_object():
    return TaskLogger([])


def get_object_with_one_data(
    description, category, status, created=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
):
    return TaskLogger(
        [
            {
                "id": 1,
                "description": description,
                "category": category,
                "status": status,
                "created": created,
            }
        ]
    )


def get_object_with_two_data(
    description_1,
    category_1,
    status_1,
    description_2,
    category_2,
    status_2,
):
    return TaskLogger(
        [
            {
                "id": 1,
                "description": description_1,
                "category": category_1,
                "status": status_1,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
            {
                "id": 2,
                "description": description_2,
                "category": category_2,
                "status": status_2,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
        ]
    )


def test_create_task_empty():
    expected = {
        "id": 1,
        "description": "test_description",
        "category": "test_category",
        "status": "pending",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    result = get_empty_object().create_task(
        description="test_description", category="test_category"
    )
    assert expected == result


def test_create_task_with_one_data():
    expected = {
        "id": 2,
        "description": "test_description",
        "category": "test_category",
        "status": "pending",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    result = get_object_with_one_data(
        description="test_description",
        category="test_category",
        status="pending",
    ).create_task(description="test_description", category="test_category")
    assert expected == result


def test_generate_summary_empty():
    expected = "Total tasks: 0\nCompleted: 0\nPending: 0"
    result = get_empty_object().generate_summary()
    assert expected == result


def test_generate_summary_with_one_data_():
    expected = "Total tasks: 1\nCompleted: 0\nPending: 1"
    result = get_object_with_one_data(
        description="test_description",
        category="test_category",
        status="pending",
    ).generate_summary()
    assert expected == result


def test_generate_summary_with_two_data_pending_and_completed():
    expected = "Total tasks: 2\nCompleted: 1\nPending: 1"
    result = get_object_with_two_data(
        description_1="test_description",
        category_1="test_category",
        status_1="pending",
        description_2="test_description_2",
        category_2="test_category_2",
        status_2="completed",
    ).generate_summary()
    assert expected == result
