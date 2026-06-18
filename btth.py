from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        if isinstance(self, FullTimeEmployee):
            emp_type = "Full-time"
        elif isinstance(self, PartTimeEmployee):
            emp_type = "Part-time"
        elif isinstance(self, InternEmployee):
            emp_type = "Intern"
        else:
            emp_type = "Unknown"

        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: {emp_type}")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def calculate_salary(self):
        return self.allowance


employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]


def display_employees(employees):
    print("--- DANH SÁCH NHÂN VIÊN ---")
    for emp in employees:
        emp.display_info()


def display_salaries(employees):
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.employee_id} | {emp.name} | Lương: {salary:,.0f} VND")


def main():
    while True:
        print("=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")
        choice = input("Chọn chức năng (1-3): ")

        match choice:
            case "1":
                display_employees(employees)
            case "2":
                display_salaries(employees)
            case "3":
                print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

main()
