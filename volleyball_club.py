# volleyball_simple.py
import json
import os
from datetime import datetime

class VolleyballClub:
    def __init__(self):
        self.children = []
        self.schedules = []
        self.payments = []
        self.current_user = None
        self.load_data()
    
    def load_data(self):
        try:
            if os.path.exists('data.json'):
                with open('data.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.children = data.get('children', [])
                    self.schedules = data.get('schedules', [])
                    self.payments = data.get('payments', [])
        except:
            pass
    
    def save_data(self):
        data = {
            'children': self.children,
            'schedules': self.schedules,
            'payments': self.payments
        }
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def clear_screen(self):
        os.system('clear')
    
    def print_header(self, title):
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{title:^60}")
        print("=" * 60 + "\n")
    
    def get_valid_choice(self, prompt, valid_choices):
        """Зөв сонголт авах"""
        while True:
            choice = input(prompt)
            if choice in valid_choices:
                return choice
            else:
                print(f" Буруу сонголт! Зөвхөн {', '.join(valid_choices)} сонгоно уу.")
    
    def main_menu(self):
        while True:
            self.print_header(" NATUR BUCKS VOLLEYBALL CLUB ")
            print("1. Admin нэвтрэх")
            print("2. Хүүхэд нэвтрэх")
            print("3. Гарах")
            print()
            
            choice = self.get_valid_choice("Сонголт оруулна уу: ", ["1", "2", "3"])
            
            if choice == "1":
                if self.admin_login():
                    self.admin_menu()
            elif choice == "2":
                if self.child_login():
                    self.child_menu()
            elif choice == "3":
                print("\n Баяртай! \n")
                break
    
    def admin_login(self):
        self.print_header(" ADMIN НЭВТРЭХ")
        
        username = input("Нэвтрэх нэр: ")
        password = input("Нууц үг: ")
        
        if username == "admin" and password == "admin123":
            self.current_user = {"type": "admin"}
            print("\n Амжилттай нэвтэрлээ!")
            input("\nEnter дарж үргэлжлүүлэх...")
            return True
        else:
            print("\n Буруу нэвтрэх мэдээлэл!")
            input("\nEnter дарж буцах...")
            return False
    
    def child_login(self):
        self.print_header(" ХҮҮХЭД НЭВТРЭХ")
        
        if not self.children:
            print(" Одоогоор бүртгэлтэй хүүхэд байхгүй байна.")
            input("\nEnter дарж буцах...")
            return False
        
        lastname = input("Овог: ")
        firstname = input("Нэр: ")
        
        for child in self.children:
            if child['lastname'].lower() == lastname.lower() and \
               child['firstname'].lower() == firstname.lower():
                self.current_user = {"type": "child", "data": child}
                print("\n Амжилттай нэвтэрлээ!")
                input("\nEnter дарж үргэлжлүүлэх...")
                return True
        
        print("\n Таны мэдээлэл олдсонгүй!")
        input("\nEnter дарж буцах...")
        return False
    
    def admin_menu(self):
        while True:
            self.print_header("ADMIN ЦОНХ")
            print("1.   Хүүхэд бүртгэх")
            print("2.   Хүүхэд устгах")
            print("3.   Бүх хүүхдийг харах")
            print("4.   Хүүхэд хайх")
            print("5.   Хуваарь үүсгэх")
            print("6.   Хуваарь өөрчлөх")
            print("7.   Хуваарь харах")
            print("8.   Төлбөр бүртгэх")
            print("9.   Төлбөрийн түүх харах")
            print("10.  Төлбөр төлөөгүй хүүхэд")
            print("0.   Буцах")
            print()
            
            choice = input("Сонголт: ")
            
            if choice == "1":
                self.add_child()
            elif choice == "2":
                self.delete_child()
            elif choice == "3":
                self.show_all_children()
            elif choice == "4":
                self.search_child()
            elif choice == "5":
                self.create_schedule()
            elif choice == "6":
                self.update_schedule()
            elif choice == "7":
                self.show_schedules()
            elif choice == "8":
                self.register_payment()
            elif choice == "9":
                self.show_payments()
            elif choice == "10":
                self.show_unpaid_children()
            elif choice == "0":
                self.current_user = None
                break
            else:
                print(" Буруу сонголт!")
                input("\nEnter дарж үргэлжлүүлэх...")
    
    def add_child(self):
        self.print_header(" ХҮҮХЭД БҮРТГЭХ")
        
        try:
            lastname = input("Овог: ")
            firstname = input("Нэр: ")
            age = int(input("Нас (6-18): "))
            if age < 6 or age > 18:
             print("\n Буруу оролт! Нас 6–18 хооронд байх ёстой.")
            input("\nEnter дарж буцах...")
            return
            
            print("\nТүвшин сонгох:")
            print("1. Анхан шат")
            print("2. Дунд шат")
            print("3. Ахисан шат")
            
            level_choice = self.get_valid_choice("Түвшин [1-3]: ", ["1", "2", "3"])
            levels = {"1": "Анхан шат", "2": "Дунд шат", "3": "Ахисан шат"}
            
            phone = input("Утас: ")
            parent_phone = input("Эцэг/эхийн утас: ")
            
            child = {
                'id': len(self.children) + 1,
                'lastname': lastname,
                'firstname': firstname,
                'age': age,
                'level': levels[level_choice],
                'phone': phone,
                'parent_phone': parent_phone,
                'registered_date': datetime.now().strftime("%Y-%m-%d")
            }
            
            self.children.append(child)
            self.save_data()
            
            print("\n Амжилттай бүртгэгдлээ!")
        except ValueError:
            print("\n Буруу оролт! Нас тоо байх ёстой.")
        except Exception as e:
            print(f"\n Алдаа гарлаа: {e}")
        
        input("\nEnter дарж үргэлжлүүлэх...")
    
    def delete_child(self):
        self.print_header("  ХҮҮХЭД УСТГАХ")
        
        if not self.children:
            print("  Бүртгэлтэй хүүхэд байхгүй байна.")
            input("\nEnter дарж буцах...")
            return
        
        self.show_all_children(pause=False)
        
        try:
            child_id = int(input("\nУстгах хүүхдийн ID: "))
            
            for i, child in enumerate(self.children):
                if child['id'] == child_id:
                    confirm = self.get_valid_choice(
                        f"Та [{child['lastname']} {child['firstname']}]-г устгахдаа итгэлтэй байна уу? (y/n): ",
                        ["y", "n", "Y", "N"]
                    )
                    if confirm.lower() == 'y':
                        self.children.pop(i)
                        self.save_data()
                        print("\n Амжилттай устгагдлаа!")
                    else:
                        print("\n Цуцлагдлаа.")
                    input("\nEnter дарж үргэлжлүүлэх...")
                    return
            
            print("\n Хүүхэд олдсонгүй!")
        except ValueError:
            print("\n Буруу оролт!")
        
        input("\nEnter дарж буцах...")
    
    def show_all_children(self, pause=True):
        self.print_header(" БҮРТГЭЛТЭЙ ХҮҮХДҮҮД")
        
        if not self.children:
            print("  Бүртгэлтэй хүүхэд байхгүй байна.")
            if pause:
                input("\nEnter дарж буцах...")
            return
        
        print(f"{'ID':<5} {'Овог':<15} {'Нэр':<15} {'Нас':<5} {'Түвшин':<15} {'Утас':<12}")
        print("-" * 80)
        
        for child in self.children:
            print(f"{child['id']:<5} {child['lastname']:<15} {child['firstname']:<15} "
                  f"{child['age']:<5} {child['level']:<15} {child['phone']:<12}")
        
        if pause:
            input("\nEnter дарж буцах...")
    
    def search_child(self):
        self.print_header(" ХҮҮХЭД ХАЙХ")
        
        search_term = input("Овог эсвэл нэрээр хайна уу: ").lower()
        
        results = [
            child for child in self.children
            if search_term in child['lastname'].lower() or 
               search_term in child['firstname'].lower()
        ]
        
        if results:
            print(f"\n Хайлтын үр дүн ({len(results)} олдлоо):\n")
            print(f"{'ID':<5} {'Овог':<15} {'Нэр':<15} {'Нас':<5} {'Түвшин':<15}")
            print("-" * 60)
            
            for child in results:
                print(f"{child['id']:<5} {child['lastname']:<15} {child['firstname']:<15} "
                      f"{child['age']:<5} {child['level']:<15}")
        else:
            print("  Хайлтад тохирох хүүхэд олдсонгүй.")
        
        input("\nEnter дарж буцах...")
    
    def create_schedule(self):
        self.print_header(" ХУВААРЬ ҮҮСГЭХ")
        
        try:
            date = input("Огноо (YYYY-MM-DD): ")
            time = input("Цаг (HH:MM): ")
            location = input("Байршил: ")
            
            print("\nТүвшин сонгох:")
            print("1. Анхан шат")
            print("2. Дунд шат")
            print("3. Ахисан шат")
            print("4. Бүгд")
            
            level_choice = self.get_valid_choice("Түвшин [1-4]: ", ["1", "2", "3", "4"])
            levels = {"1": "Анхан шат", "2": "Дунд шат", "3": "Ахисан шат", "4": "Бүгд"}
            
            schedule = {
                'id': len(self.schedules) + 1,
                'date': date,
                'time': time,
                'location': location,
                'level': levels[level_choice],
                'created_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.schedules.append(schedule)
            self.save_data()
            
            print("\n Хуваарь амжилттай үүсгэгдлээ!")
        except Exception as e:
            print(f"\n Алдаа гарлаа: {e}")
        
        input("\nEnter дарж үргэлжлүүлэх...")
    
    def update_schedule(self):
        self.print_header("  ХУВААРЬ ӨӨРЧЛӨХ")
        
        if not self.schedules:
            print("  Хуваарь байхгүй байна.")
            input("\nEnter дарж буцах...")
            return
        
        self.show_schedules(pause=False)
        
        try:
            schedule_id = int(input("\nӨөрчлөх хуваарийн ID: "))
            
            for schedule in self.schedules:
                if schedule['id'] == schedule_id:
                    print("\n Шинэ мэдээлэл оруулна уу (хоосон орхивол өмнөх утга хадгалагдана):\n")
                    
                    new_date = input(f"Огноо [{schedule['date']}]: ") or schedule['date']
                    new_time = input(f"Цаг [{schedule['time']}]: ") or schedule['time']
                    new_location = input(f"Байршил [{schedule['location']}]: ") or schedule['location']
                    
                    schedule['date'] = new_date
                    schedule['time'] = new_time
                    schedule['location'] = new_location
                    schedule['updated_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    self.save_data()
                    
                    print("\nХуваарь амжилттай өөрчлөгдлөө!")
                    input("\nEnter дарж үргэлжлүүлэх...")
                    return
            
            print("\n Хуваарь олдсонгүй!")
        except ValueError:
            print("\n Буруу оролт!")
        
        input("\nEnter дарж буцах...")
    
    def show_schedules(self, pause=True, level=None):
        self.print_header(" БЭЛТГЭЛИЙН ХУВААРЬ")
        
        if not self.schedules:
            print("  Хуваарь байхгүй байна.")
            if pause:
                input("\nEnter дарж буцах...")
            return
        
        if level:
            filtered = [s for s in self.schedules if s['level'] == level or s['level'] == "Бүгд"]
        else:
            filtered = self.schedules
        
        if not filtered:
            print(f"  {level} түвшний хуваарь байхгүй байна.")
            if pause:
                input("\nEnter дарж буцах...")
            return
        
        print(f"{'ID':<5} {'Огноо':<15} {'Цаг':<10} {'Байршил':<20} {'Түвшин':<15}")
        print("-" * 70)
        
        for schedule in filtered:
            print(f"{schedule['id']:<5} {schedule['date']:<15} {schedule['time']:<10} "
                  f"{schedule['location']:<20} {schedule['level']:<15}")
        
        if pause:
            input("\nEnter дарж буцах...")
    
    def register_payment(self):
        self.print_header(" ТӨЛБӨР БҮРТГЭХ")
        
        if not self.children:
            print(" Бүртгэлтэй хүүхэд байхгүй байна.")
            input("\nEnter дарж буцах...")
            return
        
        self.show_all_children(pause=False)
        
        try:
            child_id = int(input("\nХүүхдийн ID: "))
            
            child = next((c for c in self.children if c['id'] == child_id), None)
            
            if not child:
                print("\n Хүүхэд олдсонгүй!")
                input("\nEnter дарж буцах...")
                return
            
            amount = int(input("Төлсөн дүн (₮): "))
            
            print("\nТөлбөрийн төрөл:")
            print("1. Сар")
            print("2. Улирал")
            print("3. Жил")
            
            payment_choice = self.get_valid_choice("Төрөл [1-3]: ", ["1", "2", "3"])
            payment_types = {"1": "Сар", "2": "Улирал", "3": "Жил"}
            
            note = input("Тэмдэглэл (хоосон орхиж болно): ")
            
            payment = {
                'id': len(self.payments) + 1,
                'child_id': child_id,
                'child_name': f"{child['lastname']} {child['firstname']}",
                'amount': amount,
                'payment_type': payment_types[payment_choice],
                'payment_date': datetime.now().strftime("%Y-%m-%d"),
                'note': note
            }
            
            self.payments.append(payment)
            self.save_data()
            
            print("\n Төлбөр амжилттай бүртгэгдлээ!")
        except ValueError:
            print("\n Буруу оролт! Тоо оруулна уу.")
        except Exception as e:
            print(f"\n Алдаа гарлаа: {e}")
        
        input("\nEnter дарж үргэлжлүүлэх...")
    
    def show_payments(self):
        self.print_header(" ТӨЛБӨРИЙН ТҮҮХ")
        
        if not self.payments:
            print("  Төлбөрийн түүх байхгүй байна.")
            input("\nEnter дарж буцах...")
            return
        
        print(f"{'ID':<5} {'Хүүхэд':<30} {'Дүн':<15} {'Төрөл':<15} {'Огноо':<15}")
        print("-" * 85)
        
        for payment in self.payments:
            print(f"{payment['id']:<5} {payment['child_name']:<30} "
                  f"₮{payment['amount']:,}".ljust(15) + 
                  f"{payment['payment_type']:<15} {payment['payment_date']:<15}")
        
        input("\nEnter дарж буцах...")
    
    def show_unpaid_children(self):
        self.print_header(" ТӨЛБӨР ТӨЛӨӨГҮЙ ХҮҮХДҮҮД")
        
        if not self.children:
            print("  Бүртгэлтэй хүүхэд байхгүй байна.")
            input("\nEnter дарж буцах...")
            return
        
        paid_children_ids = set(p['child_id'] for p in self.payments)
        unpaid = [c for c in self.children if c['id'] not in paid_children_ids]
        
        if not unpaid:
            print(" Бүх хүүхэд төлбөрөө төлсөн байна!")
            input("\nEnter дарж буцах...")
            return
        
        print(f"  Төлбөр төлөөгүй хүүхдүүд ({len(unpaid)}):\n")
        print(f"{'ID':<5} {'Овог':<15} {'Нэр':<15} {'Түвшин':<15} {'Утас':<12}")
        print("-" * 65)
        
        for child in unpaid:
            print(f"{child['id']:<5} {child['lastname']:<15} {child['firstname']:<15} "
                  f"{child['level']:<15} {child['phone']:<12}")
        
        input("\nEnter дарж буцах...")
    
    def child_menu(self):
        child_data = self.current_user['data']
        
        while True:
            self.print_header(f"👋 ТАВТАЙ МОРИЛ, {child_data['firstname']}!")
            print("1.  Миний хуваарь харах")
            print("2.  Миний мэдээлэл")
            print("0.  Буцах")
            print()
            
            choice = self.get_valid_choice("Сонголт: ", ["1", "2", "0"])
            
            if choice == "1":
                self.show_schedules(pause=True, level=child_data['level'])
            elif choice == "2":
                self.show_child_info()
            elif choice == "0":
                self.current_user = None
                break
    
    def show_child_info(self):
        child = self.current_user['data']
        self.print_header("МИНИЙ МЭДЭЭЛЭЛ")
        
        print(f"Овог:                {child['lastname']}")
        print(f"Нэр:                 {child['firstname']}")
        print(f"Нас:                 {child['age']}")
        print(f"Түвшин:              {child['level']}")
        print(f"Утас:                {child['phone']}")
        print(f"Эцэг/Эхийн утас:     {child['parent_phone']}")
        print(f"Бүртгэгдсэн огноо:   {child['registered_date']}")
        
        child_payments = [p for p in self.payments if p['child_id'] == child['id']]
        
        if child_payments:
            print("\n Төлбөрийн түүх:")
            print(f"{'Огноо':<15} {'Дүн':<15} {'Төрөл':<15}")
            print("-" * 45)
            
            for p in child_payments:
                print(f"{p['payment_date']:<15} ₮{p['amount']:,}".ljust(15) + f"{p['payment_type']:<15}")
        else:
            print("\n  Төлбөрийн түүх байхгүй байна.")
        
        input("\nEnter дарж буцах...")


def main():
    print("\n" + "=" * 60)
    print(" NATUR BUCKS VOLLEYBALL CLUB ".center(60))
    print("Бүртгэлийн систем".center(60))
    print("=" * 60 + "\n")
    input("Enter дарж эхлүүлэх...")
    
    club = VolleyballClub()
    club.main_menu()


if __name__ == "__main__":
    main()