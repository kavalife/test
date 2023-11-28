#include <iostream>
#include <vector>
#include <string>
#include <Windows.h>

// Клас, що представляє нерухомість
class RealEstate {
public:
    std::string address;  // Адреса нерухомості
    std::string type;     // Тип нерухомості
    double price;         // Вартість нерухомості

    // Конструктор для ініціалізації об'єкту нерухомості
    RealEstate(const std::string& addr, const std::string& t, double p)
        : address(addr), type(t), price(p) {}

    // Метод для відображення інформації про нерухомість
    void display() const {
        std::cout << "Адреса: " << address << ", Тип нерухомості: " << type << ", Вартість: $" << price << std::endl;
    }
};

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    std::vector<RealEstate> realEstates;  // Вектор для зберігання об'єктів нерухомості
    char choice;

    do {
        // Виведення меню
        std::cout << "Твоя агенція нерухомості" << std::endl;
        std::cout << "1. Додати об'єкт" << std::endl;
        std::cout << "2. Показати перелік об'єктів" << std::endl;
        std::cout << "0. Вихід" << std::endl;
        std::cout << "Зробіть вибір: ";
        std::cin >> choice;

        switch (choice) {
            case '1': {
                std::string address, type;
                double price;

                // Введення даних для нового об'єкту нерухомості
                std::cin.ignore();
                std::cout << "Введіть адресу: ";
                std::getline(std::cin, address);
                std::cout << "Введіть тип нерухомості: ";
                std::getline(std::cin, type);
                std::cout << "Введіть вартість: ";
                std::cin >> price;

                // Створення та додавання нового об'єкту нерухомості до вектору
                RealEstate newRealEstate(address, type, price);
                realEstates.push_back(newRealEstate);
                std::cout << "Об'єкт додано успішно." << std::endl;
                break;
            }
            case '2':
                // Виведення переліку внесених об'єктів нерухомості
                std::cout << "Список внесених об'єктів:" << std::endl;
                for (const RealEstate& property : realEstates) {
                    property.display();
                }
                break;
            case '3':
                std::cout << "Бувай!" << std::endl;
                break;
            default:
                std::cout << "Помилковий вибір, спробуйте ще раз" << std::endl;
        }
    } while (choice != '0');

    return 0;
}
