
class Animal {

     Animal() {
        System.out.println("Constructor of Animal class");
    }

    Animal(int a) {
        System.out.println("Parameterised constructor of Animal a=" + a);
    }

    void eat() {
        System.out.println("Animal is eating");
    }
}

class Dog extends Animal {
    Dog() {
        super(4);
        System.out.println("Constructor of Dog class");
    }

    void bark() {
        System.out.println("Dog is barking");
    }
}

public class SingleInheritance {
    public static void main(String[] args) {

        Dog d = new Dog();

        d.eat();
        d.bark();
    }
}