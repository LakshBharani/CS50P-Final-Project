from project import add_task, update_task, delete_task

def main():
    test_add_task()
    test_update_task()
    test_delete_task()

def test_add_task():
    assert add_task(1, "Cs50p", "Do cs50p project by tonight", "H", "N") == True
    assert add_task(1, "Lunch", "Have lunch with friends", "", "N") == False

def test_update_task():
    assert update_task(1, "Y") == True
    assert update_task("", "Y") == False
    assert update_task(2, "") == False

def test_delete_task():
    assert delete_task([['Task ID', 'Task Label', 'Task Description', 'Task Priority', 'Task Status'], [1, 'Cs50P', 'Do project', 'H', 'N'], [2, 'Lunch', 'Go to lunch with friends', 'M', 'N'], [3, 'Go Karting', 'Go to Ezone with family', 'L', 'N'], [4, 'Birthday Party', 'Call organisers to host friends 19th birthday', 'H', 'N'], [5, 'Homework', 'Do math homework', 'M', 'N']], 1) == [['Task ID', 'Task Label', 'Task Description', 'Task Priority', 'Task Status'], [2, 'Lunch', 'Go to lunch with friends', 'M', 'N'], [3, 'Go Karting', 'Go to Ezone with family', 'L', 'N'], [4, 'Birthday Party', 'Call organisers to host friends 19th birthday', 'H', 'N'], [5, 'Homework', 'Do math homework', 'M', 'N']]
    assert delete_task([['Task ID', 'Task Label', 'Task Description', 'Task Priority', 'Task Status'], [1, 'Cs50P', 'Do project', 'H', 'N'], [2, 'Lunch', 'Go to lunch with friends', 'M', 'N'], [3, 'Go Karting', 'Go to Ezone with family', 'L', 'N'], [4, 'Birthday Party', 'Call organisers to host friends 19th birthday', 'H', 'N'], [5, 'Homework', 'Do math homework', 'M', 'N']], 5) == [['Task ID', 'Task Label', 'Task Description', 'Task Priority', 'Task Status'], [1, 'Cs50P', 'Do project', 'H', 'N'], [2, 'Lunch', 'Go to lunch with friends', 'M', 'N'], [3, 'Go Karting', 'Go to Ezone with family', 'L', 'N'], [4, 'Birthday Party', 'Call organisers to host friends 19th birthday', 'H', 'N']]

if __name__ == "__main__":
    main()