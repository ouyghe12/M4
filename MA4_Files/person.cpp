#include <cstdlib>
// Person class 

class Person{
public:
	Person(int);
	int get();
	void set(int);
	int fibonacci(int n);
private:
	int age;
};
Person::Person(int n){
	age = n;
}
int Person::get(){
	return age;
}
void Person::set(int n){
	age = n;
}
int Person::fibonacci(int n) {
	if (n <= 1) {
		return n;
	}else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fibonacci(Person* person) {
	return person->fibonacci(person->get());
 }
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
}
