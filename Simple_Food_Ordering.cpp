#include <iostream>
using namespace std;
int main()
{
    int choice, ch;
    string name;
    cout << "------- Tops_Devanshu Fast Food -------" << endl;

    cout << "Please Enter Your Name : ";
    cin >> name;
    cout << "Hello " << name << endl;
    cout << "---------------------------------------------------------" << endl;
    cout << "What Would You like to Order ? " << endl;
    cout << endl;
    cout << "------- MENU -------" << endl;
    cout << endl;
    cout << "1) PIZZAS...." << endl;
    cout << "2) BURGERS...." << endl;
    cout << "3) SANDWICH...." << endl;
    cout << "4) ROLLS...." << endl;
    cout << "5) BIRYANI...." << endl;
    cout << endl;
    cout << "---------------------------------------------------------" << endl;
    cout << "Please Enter Your Choice : ";
    cin >> choice;
    cout << "---------------------------------------------------------" << endl;
    switch (choice)
    {
    case 1:
        cout << "1) Pizza X Rs. 240" << endl;
        cout << "2) Pizza Y Rs. 160" << endl;
        cout << "3) Pizza Z Rs.100" << endl;
        break;
    case 2:
        cout << "1) Burgers X Rs. 240" << endl;
        cout << "2) Burgers Y Rs. 160" << endl;
        cout << "3) Burgers Z Rs.100" << endl;
        break;
    case 3:
        cout << "1) Club Sandwich Rs. 240" << endl;
        cout << "2) Veg. Crispy Sandwich Rs. 160" << endl;
        cout << "3) Extream Veg Sandwich Rs.100" << endl;
        break;
    case 4:
        cout << "1) Rolls X Rs. 240" << endl;
        cout << "2) Rolls Y Rs. 160" << endl;
        cout << "3) Rolls Z Rs.100" << endl;
        break;
    case 5:
        cout << "1) Biryani X Rs. 240" << endl;
        cout << "2) Biryani Y Rs. 160" << endl;
        cout << "3) Biryani Z Rs.100" << endl;
        break;

    default:
        cout << "You Enter Wrong Choice....";
        break;
    }
    // switch (ch)
    // {
    // case /* constant-expression */:
    //     /* code */
    //     break;

    // default:
    //     break;
    // }

    return 0;
}