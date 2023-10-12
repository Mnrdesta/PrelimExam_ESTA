import math

def test_obese():
    weight = 85
    assert weight >= 80

def test_temp():
    kelvin = 5
    celsius = kelvin + 32
    fahrenheit = (celsius * 9/5) + 32
    assert fahrenheit == 98

def test_triangle():
    base = 5 
    heigth = 4
    area = base * heigth
    assert area == 20

if __name__ == '__main__':
    math.main()