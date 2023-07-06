from unittest import TestCase, main

from Proxy_coding_exercise import ResponsiblePerson, Person


class TestResponsiblePerson(TestCase):

    def test_juan(self):
        juan = ResponsiblePerson(Person(20))
        self.assertEqual(juan.drive(), "driving")
        self.assertEqual(juan.drink(), "drinking")
        self.assertEqual(juan.drink_and_drive(), "dead")

    def test_pepe(self):
        pepe = ResponsiblePerson(Person(17))
        self.assertEqual(pepe.drive(), "driving")
        self.assertEqual(pepe.drink(), "too young")
        self.assertEqual(pepe.drink_and_drive(), "dead")        

    def test_bob(self):
        bob = ResponsiblePerson(Person(15))
        self.assertEqual(bob.drive(), "too young")
        self.assertEqual(bob.drink(), "too young")
        self.assertEqual(bob.drink_and_drive(), "dead")

    def test_exercise(self):
        p = Person(10)
        rp = ResponsiblePerson(p)

        self.assertEqual('too young', rp.drive())
        self.assertEqual('too young', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())

        rp.age = 20

        self.assertEqual('driving', rp.drive())
        self.assertEqual('drinking', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())    

if __name__ == "__main__":
    main()