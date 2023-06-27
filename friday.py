import pyttsx3
import speech_recognition as sr
from datetime import date
import time
import webbrowser
import datetime
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
#import Gesture_Controller
#import Gesture_Controller_Gloved as Gesture_Controller
import app
from threading import Thread


# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()
keyboard = Controller()
engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# ----------------Variables------------------------
file_exp_status = False
files =["E:\Windows\Hey Atanu Welcome.mp3"]
path = 'E:\Windows'
is_awake = True  #Bot status

# ------------------Functions----------------------
def reply(audio):
    app.ChatBot.addAppMsg(audio)

    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        reply("Good Morning !")
    elif hour>=12 and hour<18:
        reply("Good Afternoon !")   
    else:
        reply("Good Evening !")  
        
    reply("I am friday, What can i do for you Atanu!")

# Set Microphone parameters
with sr.Microphone() as source:
        r.energy_threshold = 500 
        r.dynamic_energy_threshold = False

# Audio to String
def record_audio():
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)

        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry my Service is down. Plz check your Internet connection')
        except sr.UnknownValueError:
            print('cant recognize')
            pass
        return voice_data.lower()


#Respond

    
def respond(voice_data):
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('friday','')
    app.eel.addUserMsg(voice_data)

    if is_awake==False:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    elif 'hello' in voice_data:
        wish()
    
    elif 'hey friday' in voice_data:
        reply('Hey Atanu Whats up!')

    elif 'date of birth' in voice_data:
        reply('22-05-1999!')
        
    elif 'my name' in voice_data:
        reply('your name is Atanu Roy!')

    elif 'your name' in voice_data:
        reply('My name is friday i am build by Atanu!')
    
    elif 'i love you' in voice_data:
        reply('I  love you too Atanu!')

    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])
    
    elif 'chrome' in voice_data:
        reply('Opening ' + voice_data.split('chrome')[1])
        url = 'https://www.google.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'google' in voice_data:
        reply('Opening ' + voice_data.split('google')[1])
        url = 'https://www.google.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'youtube' in voice_data:
        reply('Opening ' + voice_data.split('youtube')[1])
        url = 'https://www.youtube.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'git hub' in voice_data:
        reply('Opening ' + voice_data.split('git hub')[1])
        url = 'https://github.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'whatsapp' in voice_data:
        reply('Opening ' + voice_data.split('whatsapp')[1])
        url = 'https://web.whatsapp.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'chat gpt' in voice_data:
        reply('Opening ' + voice_data.split('chat gpt')[1])
        url = 'https://chat.openai.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'facebook' in voice_data:
        reply('Opening ' + voice_data.split('facebook')[1])
        url = 'https://www.facebook.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'code pen' in voice_data:
        reply('Opening ' + voice_data.split('code pen')[1])
        url = 'https://codepen.io/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'cartoon' in voice_data:
        reply('Opening ' + voice_data.split('cartoon')[1])
        url = 'https://www.youtube.com/results?search_query=cartoon'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')
    elif 'music' in voice_data:
        reply('Opening ' + voice_data.split('music')[1])
        url = 'https://www.youtube.com/results?search_query=music'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')        
    elif 'song' in voice_data:
        reply('Opening ' + voice_data.split('song')[1])
        url = 'https://www.youtube.com/results?search_query=songs'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')  
    elif 'telegram' in voice_data:
        reply('Opening ' + voice_data.split('telegram')[1])
        url = 'https://web.telegram.org/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'gmail' in voice_data:
        reply('Opening ' + voice_data.split('gmail')[1])
        url = 'https://mail.google.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')
    
    elif 'football' in voice_data:
        reply('Opening ' + voice_data.split('football')[1])
        url = 'https://www.goal.com/en-in/live-scores'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'cricket' in voice_data:
        reply('Opening ' + voice_data.split('cricket')[1])
        url = 'https://www.cricbuzz.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'recipe' in voice_data:
        reply('Opening ' + voice_data.split('recipe')[1])
        url = 'https://www.youtube.com/results?search_query=recipe'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'news' in voice_data:
        reply('Opening ' + voice_data.split('news')[1])
        url = 'https://bengali.abplive.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'how are you' in voice_data:
        reply("I'm doing great, thank you!")

    elif 'weather' in voice_data:
        reply("The weather is sunny and clear today.")

    elif 'inspire me' in voice_data or 'quote of the day' in voice_data:
        reply("Why don't scientists trust atoms? Because they make up everything!")

    elif 'capital of india' in voice_data:
        reply("The capital of india is New Delhi.")

    elif 'capital of west bengal' in voice_data:
        reply("The capital of india is New kolkata.")
        
    elif 'thank you' in voice_data:
        reply("You're welcome! I'm here to help.")



    # java# java # java # java # java # java # java

    elif 'what is java' in voice_data:
        reply("Java is a high-level, object-oriented programming language.")
    elif 'difference between jdk and jre' in voice_data:
        reply("JDK (Java Development Kit) is a software development kit that provides tools, libraries, and compilers for developing Java applications. JRE (Java Runtime Environment) is an environment that enables the execution of Java applications.")
    elif 'main features of java' in voice_data:
        reply("1. Object-oriented: Java follows an object-oriented programming paradigm. 2. Platform-independent: Java programs can run on any platform that has a Java Virtual Machine. 3. Garbage collection: Java automatically manages memory through garbage collection. 4. Exception handling: Java provides built-in exception handling mechanisms. 5. Multithreading: Java supports concurrent programming through multithreading.")
    elif 'class in java' in voice_data:
        reply("In Java, a class is a blueprint or a template for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class can have. For example, you can create a class named Main with a variable x: public class Main { int x = 5; }")
    elif "interface in java" in voice_data:
        reply("An interface in Java is a collection of abstract methods. It defines a contract for classes that implement it.")
    elif "inheritance in java" in voice_data:
        reply("Inheritance is a mechanism in Java where a class can inherit the properties and methods of another class.")
    elif "polymorphism in java" in voice_data:
        reply("Polymorphism is the ability of an object to take on multiple forms. It can be achieved through method overloading and method overriding in Java.")
    elif "exception in java" in voice_data:
        reply("An exception is an event that occurs during the execution of a program and disrupts the normal flow of instructions. Java provides exception handling mechanisms to handle such exceptions.")
    elif "constructor in java" in voice_data:
        reply("A constructor is a special method in a class that is used to initialize objects. It is called when an object of the class is created.")
    elif "main method in java" in voice_data:
        reply("The main() method is the entry point of a Java program. It is the method that is executed when the program starts running.")
    elif "method in java" in voice_data:
        reply("A method in Java is a set of instructions that can be called to perform a specific task. It is a reusable block of code.")
    elif "encapsulation in java" in voice_data:
        reply("Encapsulation is the process of hiding the internal details of an object and providing access only through public methods. It helps in achieving data abstraction and data security.")
    elif "package in java" in voice_data:
        reply("A package in Java is a way of organizing related classes and interfaces. It provides a namespace for the classes to avoid naming conflicts.")
    elif "loop in java" in voice_data:
        reply("A loop in Java is a control structure that allows the execution of a block of code repeatedly until a certain condition is met. Commonly used loops in Java are the for loop, while loop, and do-while loop.")
    elif "method overloading in java" in voice_data:
        reply("Method overloading in Java is the ability to define multiple methods with the same name but different parameters. It allows a class to have methods with similar functionalities but different input arguments.")
    elif "method overriding in java" in voice_data:
        reply("Method overriding in Java is the ability to provide a different implementation of a method in a subclass that is already defined in its superclass. It allows the subclass to provide its own implementation of the inherited method.")
    elif "thread in java" in voice_data:
        reply("A thread in Java is a lightweight unit of execution within a program. It allows multiple tasks to be performed concurrently, improving the efficiency and responsiveness of an application. Threads can be used to perform time-consuming operations without blocking the main execution flow.")
    elif "synchronized keyword in java" in voice_data:
        reply("The 'synchronized' keyword in Java is used to create mutually exclusive blocks of code. It ensures that only one thread can execute a synchronized block at a time, preventing concurrent access and potential data inconsistencies in multithreaded programs.")
    elif "exception in java" in voice_data:
        reply("In Java, an exception is an event that occurs during the execution of a program and disrupts the normal flow of instructions. Exceptions can be caused by various factors, such as invalid input, resource unavailability, or programming errors. Java provides exception handling mechanisms to catch and handle these exceptions, preventing abrupt termination of the program.")
    elif "try-catch block in java" in voice_data:
        reply("The try-catch block in Java is used for exception handling. It allows developers to write code that can potentially throw an exception within the try block and provide specific error-handling logic in the catch block. If an exception occurs within the try block, the catch block with a matching exception type is executed.")
    elif "finally block in java" in voice_data:
        reply("The finally block in Java is used in conjunction with the try-catch block for exception handling. It contains code that is always executed, regardless of whether an exception is thrown or caught. The finally block is typically used to release resources, such as closing files or network connections.")
    elif 'different types of variables in java' in voice_data:
        reply("Instance variable, local variable, and class variable are the different types of variables in Java.")
    elif 'declare and use an array in java' in voice_data:
        reply("To declare and use an array in Java, you can use the following code example:\n\nint[] numbers = {1, 2, 3, 4, 5};\nint firstElement = numbers[0];\nint length = numbers.length;")
    elif 'if-else statement in java' in voice_data:
        reply("To use the if-else statement in Java, you can use the following code example:\n\nint number = 10;\n\nif (number > 0) {\n    System.out.println('The number is positive.');\n} else if (number < 0) {\n    System.out.println('The number is negative.');\n} else {\n    System.out.println('The number is zero.');\n}")
    elif 'for loop in java' in voice_data:
        reply("A for loop in Java allows you to repeatedly execute a block of code for a specified number of times. Here's an example:\n\nfor (int i = 1; i <= 5; i++) {\n    System.out.println('Iteration: ' + i);\n}")
    elif 'define and call a method in java' in voice_data:
        reply("To define and call a method in Java, you can use the following code example:\n\nvoid greet() {\n    System.out.println('Hello, world!');\n}\n\ngreet();")
    elif 'while loop in java' in voice_data:
        reply("A while loop in Java allows you to repeatedly execute a block of code as long as a specified condition is true. Here's an example:\n\nint i = 1;\n\nwhile (i <= 5) {\n    System.out.println('Iteration: ' + i);\n    i++;\n}")
    elif 'break statement in java' in voice_data:
        reply("The 'break' statement in Java is used to exit a loop prematurely. It is often used to terminate a loop when a certain condition is met. Here's an example:\n\nfor (int i = 1; i <= 10; i++) {\n    if (i == 6) {\n        break; // Exit the loop when i is 6\n    }\n    System.out.println('Iteration: ' + i);\n}")
    elif 'class with a constructor in java' in voice_data:
        reply("To define a class with a constructor in Java, you can use the following code example:\n\nclass Person {\n    String name;\n\n    Person(String personName) {\n        name = personName;\n    }\n}\n\nPerson person = new Person('John');")
    elif 'this keyword in java' in voice_data:
        reply("The 'this' keyword in Java is used to refer to the current instance of a class. It is often used to differentiate between instance variables and method parameters with the same name. Here's an example:\n\nclass Rectangle {\n    int width;\n    int height;\n\n    Rectangle(int width, int height) {\n        this.width = width;\n        this.height = height;\n    }\n}")
    elif 'handle exceptions using try-catch blocks in java' in voice_data:
        reply("To handle exceptions using try-catch blocks in Java, you can use the following code example:\n\ntry {\n    // Code that may throw an exception\n    int result = divide(10, 0);\n    System.out.println('Result: ' + result);\n} catch (ArithmeticException e) {\n    // Handling the exception\n    System.out.println('Error: ' + e.getMessage());\n}")
    elif 'exceptio handelling in java' in voice_data:
        reply("To handle exceptions using try-catch blocks in Java, you can use the following code example:\n\ntry {\n    // Code that may throw an exception\n    int result = divide(10, 0);\n    System.out.println('Result: ' + result);\n} catch (ArithmeticException e) {\n    // Handling the exception\n    System.out.println('Error: ' + e.getMessage());\n}")
    elif 'try-catch in java' in voice_data:
        reply("To handle exceptions using try-catch blocks in Java, you can use the following code example:\n\ntry {\n    // Code that may throw an exception\n    int result = divide(10, 0);\n    System.out.println('Result: ' + result);\n} catch (ArithmeticException e) {\n    // Handling the exception\n    System.out.println('Error: ' + e.getMessage());\n}")
    elif 'create a file in java' in voice_data:
        reply("To create a file in Java, you can use the following code example:\n\nimport java.io.File;\nimport java.io.IOException;\n\npublic class CreateFileExample {\n    public static void main(String[] args) {\n        try {\n            File file = new File('example.txt');\n            if (file.createNewFile()) {\n                System.out.println('File created successfully.');\n            } else {\n                System.out.println('File already exists.');\n            }\n        } catch (IOException e) {\n            System.out.println('An error occurred: ' + e.getMessage());\n        }\n    }\n}")
    elif 'read data from a file in java' in voice_data:
        reply("To read data from a file in Java, you can use the following code example:\n\nimport java.io.File;\nimport java.io.FileNotFoundException;\nimport java.util.Scanner;\n\npublic class ReadFileExample {\n    public static void main(String[] args) {\n        try {\n            File file = new File('example.txt');\n            Scanner scanner = new Scanner(file);\n\n            while (scanner.hasNextLine()) {\n                String line = scanner.nextLine();\n                System.out.println(line);\n            }\n\n            scanner.close();\n        } catch (FileNotFoundException e) {\n            System.out.println('File not found: ' + e.getMessage());\n        }\n    }\n}")
    elif 'write data to a file in java' in voice_data:
        reply("To write data to a file in Java, you can use the following code example:\n\nimport java.io.FileWriter;\nimport java.io.IOException;\n\npublic class WriteFileExample {\n    public static void main(String[] args) {\n        try {\n            FileWriter writer = new FileWriter('example.txt');\n            writer.write('Hello, world!');\n            writer.close();\n            System.out.println('Data written to the file successfully.');\n        } catch (IOException e) {\n            System.out.println('An error occurred: ' + e.getMessage());\n        }\n    }\n}")
    elif 'create a directory in java' in voice_data:
        reply("To create a directory in Java, you can use the following code example:\n\nimport java.io.File;\n\npublic class CreateDirectoryExample {\n    public static void main(String[] args) {\n        File directory = new File('example');\n\n        if (directory.mkdir()) {\n            System.out.println('Directory created successfully.');\n        } else {\n            System.out.println('Failed to create directory.');\n        }\n    }\n}")
    elif 'list files in a directory in java' in voice_data:
        reply("To list files in a directory in Java, you can use the following code example:\n\nimport java.io.File;\n\npublic class ListFilesExample {\n    public static void main(String[] args) {\n        File directory = new File('example');\n\n        File[] files = directory.listFiles();\n\n        if (files != null) {\n            for (File file : files) {\n                System.out.println(file.getName());\n            }\n        }\n    }\n}")
    elif 'sort an array in java' in voice_data:
        reply("To sort an array in Java, you can use the following code example:\n\nimport java.util.Arrays;\n\npublic class SortArrayExample {\n    public static void main(String[] args) {\n        int[] array = {5, 2, 8, 1, 4};\n        Arrays.sort(array);\n        System.out.println('Sorted array: ' + Arrays.toString(array));\n    }\n}")
    elif 'factorial of a number in java' in voice_data:
        reply("To calculate the factorial of a number in Java, you can use the following code example:\n\npublic class FactorialExample {\n    public static void main(String[] args) {\n        int number = 5;\n        int factorial = 1;\n\n        for (int i = 1; i <= number; i++) {\n            factorial *= i;\n        }\n\n        System.out.println('Factorial of ' + number + ' is: ' + factorial);\n    }\n}")
    elif 'reverse a string in java' in voice_data:
        reply("To reverse a string in Java, you can use the following code example:\n\npublic class ReverseStringExample {\n    public static void main(String[] args) {\n        String str = 'Hello, world!';\n        String reversed = '';\n\n        for (int i = str.length() - 1; i >= 0; i--) {\n            reversed += str.charAt(i);\n        }\n\n        System.out.println('Reversed string: ' + reversed);\n    }\n}")
    elif 'sum of digits in a number in java' in voice_data:
        reply("To calculate the sum of digits in a number in Java, you can use the following code example:\n\npublic class SumOfDigitsExample {\n    public static void main(String[] args) {\n        int number = 12345;\n        int sum = 0;\n\n        while (number > 0) {\n            int digit = number % 10;\n            sum += digit;\n            number /= 10;\n        }\n\n        System.out.println('Sum of digits: ' + sum);\n    }\n}")
    elif 'maximum element in an array in java' in voice_data:
        reply("To find the maximum element in an array in Java, you can use the following code example:\n\npublic class MaxElementExample {\n    public static void main(String[] args) {\n        int[] array = {5, 2, 8, 1, 4};\n        int max = array[0];\n\n        for (int i = 1; i < array.length; i++) {\n            if (array[i] > max) {\n                max = array[i];\n            }\n        }\n\n        System.out.println('Maximum element: ' + max);\n    }\n}")
    elif 'prime in java' in voice_data:
        reply("To check if a number is prime in Java, you can use the following code example:\n\npublic class PrimeNumberExample {\n    public static void main(String[] args) {\n        int number = 17;\n        boolean isPrime = true;\n\n        for (int i = 2; i <= Math.sqrt(number); i++) {\n            if (number % i == 0) {\n                isPrime = false;\n                break;\n            }\n        }\n\n        if (isPrime) {\n            System.out.println(number + ' is a prime number.');\n        } else {\n            System.out.println(number + ' is not a prime number.');\n        }\n    }\n}")
    elif 'fibonacci series in java' in voice_data:
        reply("To calculate the Fibonacci series in Java, you can use the following code example:\n\npublic class FibonacciSeriesExample {\n    public static void main(String[] args) {\n        int count = 10;\n        int first = 0;\n        int second = 1;\n\n        System.out.print('Fibonacci Series: ' + first + ', ' + second);\n\n        for (int i = 2; i < count; i++) {\n            int next = first + second;\n            System.out.print(', ' + next);\n            first = second;\n            second = next;\n        }\n    }\n}")
    elif 'reverse an array in java' in voice_data:
        reply("To reverse an array in Java, you can use the following code example:\n\npublic class ReverseArrayExample {\n    public static void main(String[] args) {\n        int[] array = {1, 2, 3, 4, 5};\n        int length = array.length;\n\n        for (int i = 0; i < length / 2; i++) {\n            int temp = array[i];\n            array[i] = array[length - 1 - i];\n            array[length - 1 - i] = temp;\n        }\n\n        System.out.println('Reversed array: ' + Arrays.toString(array));\n    }\n}")
    elif 'check if a string is a palindrome in java' in voice_data:
        reply("To check if a string is a palindrome in Java, you can use the following code example:\n\npublic class PalindromeExample {\n    public static void main(String[] args) {\n        String str = 'madam';\n        boolean isPalindrome = true;\n\n        for (int i = 0; i < str.length() / 2; i++) {\n            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) {\n                isPalindrome = false;\n                break;\n            }\n        }\n\n        if (isPalindrome) {\n            System.out.println(str + ' is a palindrome.');\n        } else {\n            System.out.println(str + ' is not a palindrome.');\n        }\n    }\n}")
    elif 'power of a number in java' in voice_data:
        reply("To calculate the power of a number in Java, you can use the following code example:\n\npublic class PowerExample {\n    public static void main(String[] args) {\n        int base = 2;\n        int exponent = 3;\n        int result = 1;\n\n        for (int i = 0; i < exponent; i++) {\n            result *= base;\n        }\n\n        System.out.println(base + ' raised to the power of ' + exponent + ' is: ' + result);\n    }\n}")
    elif 'armstrong in java' in voice_data:
        reply("To check if a number is Armstrong in Java, you can use the following code example:\n\npublic class ArmstrongNumberExample {\n    public static void main(String[] args) {\n        int number = 153;\n        int originalNumber = number;\n        int result = 0;\n        int n = String.valueOf(number).length();\n\n        while (number != 0) {\n            int remainder = number % 10;\n            result += Math.pow(remainder, n);\n            number /= 10;\n        }\n\n        if (result == originalNumber) {\n            System.out.println(originalNumber + ' is an Armstrong number.');\n        } else {\n            System.out.println(originalNumber + ' is not an Armstrong number.');\n        }\n    }\n}")
    elif 'factorial of a number using recursion in java' in voice_data:
        reply("To find the factorial of a number using recursion in Java, you can use the following code example:\n\npublic class RecursiveFactorialExample {\n    public static void main(String[] args) {\n        int number = 5;\n        int factorial = factorial(number);\n\n        System.out.println('Factorial of ' + number + ' is: ' + factorial);\n    }\n\n    public static int factorial(int number) {\n        if (number == 0) {\n            return 1;\n        }\n\n        return number * factorial(number - 1);\n    }\n}")
    if 'find the maximum number in an array in java' in voice_data:
        reply("To find the maximum number in an array in Java, you can use the following code example:\n\npublic class MaximumNumberExample {\n    public static void main(String[] args) {\n        int[] numbers = {5, 8, 2, 10, 3};\n        int max = numbers[0];\n\n        for (int i = 1; i < numbers.length; i++) {\n            if (numbers[i] > max) {\n                max = numbers[i];\n            }\n        }\n\n        System.out.println('Maximum number: ' + max);\n    }\n}")
    elif 'sort an array in ascending order in java' in voice_data:
        reply("To sort an array in ascending order in Java, you can use the Arrays.sort() method. Here's an example:\n\nimport java.util.Arrays;\n\npublic class ArraySortExample {\n    public static void main(String[] args) {\n        int[] numbers = {5, 2, 8, 3, 1};\n\n        Arrays.sort(numbers);\n\n        System.out.println('Sorted array: ' + Arrays.toString(numbers));\n    }\n}")
    elif 'average of numbers in an array in java' in voice_data:
        reply("To calculate the average of numbers in an array in Java, you can use the following code example:\n\npublic class AverageExample {\n    public static void main(String[] args) {\n        int[] numbers = {5, 2, 8, 3, 1};\n        int sum = 0;\n\n        for (int number : numbers) {\n            sum += number;\n        }\n\n        double average = (double) sum / numbers.length;\n\n        System.out.println('Average: ' + average);\n    }\n}")
    elif 'string contains a substring in java' in voice_data:
        reply("To check if a string contains a substring in Java, you can use the contains() method. Here's an example:\n\npublic class SubstringCheckExample {\n    public static void main(String[] args) {\n        String input = 'Hello, World!';\n        String substring = 'World';\n        boolean containsSubstring = input.contains(substring);\n\n        System.out.println('Contains substring: ' + containsSubstring);\n    }\n}")
    elif 'reverse a string in java' in voice_data:
        reply("To reverse a string in Java, you can use the following code example:\n\npublic class StringReverseExample {\n    public static void main(String[] args) {\n        String input = 'Hello, World!';\n        String reversed = new StringBuilder(input).reverse().toString();\n\n        System.out.println('Reversed string: ' + reversed);\n    }\n}")
    elif 'year is a leap year or not in java' in voice_data:
        reply("To check if a year is a leap year in Java, you can use the following code example:\n\npublic class LeapYearCheckExample {\n    public static void main(String[] args) {\n        int year = 2024;\n        boolean isLeapYear = false;\n\n        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {\n            isLeapYear = true;\n        }\n\n        System.out.println('Is leap year: ' + isLeapYear);\n    }\n}")
    elif 'largest element in an array in java' in voice_data:
        reply("To find the largest element in an array in Java, you can use the following code example:\n\npublic class LargestElementExample {\n    public static void main(String[] args) {\n        int[] array = {5, 3, 9, 2, 7};\n        int largest = array[0];\n\n        for (int i = 1; i < array.length; i++) {\n            if (array[i] > largest) {\n                largest = array[i];\n            }\n        }\n\n        System.out.println('Largest element: ' + largest);\n    }\n}")
    elif 'convert a string to lowercase in java' in voice_data:
        reply("To convert a string to lowercase in Java, you can use the toLowerCase() method of the String class. Here's an example:\n\npublic class StringToLowercaseExample {\n    public static void main(String[] args) {\n        String input = 'Hello World';\n        String lowercase = input.toLowerCase();\n\n        System.out.println('Lowercase string: ' + lowercase);\n    }\n}")
    elif 'length of a string in java' in voice_data:
        reply("To find the length of a string in Java, you can use the length() method of the String class. Here's an example:\n\npublic class StringLengthExample {\n    public static void main(String[] args) {\n        String input = 'Hello World';\n        int length = input.length();\n\n        System.out.println('Length of string: ' + length);\n    }\n}")
    elif 'binary to decimal in java' in voice_data:
        reply("To convert a binary number to decimal in Java, you can use the following code example:\n\npublic class BinaryToDecimalExample {\n    public static void main(String[] args) {\n        String binary = '101010';\n        int decimal = Integer.parseInt(binary, 2);\n\n        System.out.println('Decimal: ' + decimal);\n    }\n}")
    elif 'random number in java' in voice_data:
        reply("generate a random number in Java, you can use the java.util.Random class. Here's an example:\n\nimport java.util.Random;\n\npublic class RandomNumberExample {\n    public static void main(String[] args) {\n        Random random = new Random();\n        int randomNumber = random.nextInt(10); // Generates a random number between 0 and 9\n\n        System.out.println('Random number: ' + randomNumber);\n    }\n}")
    elif 'square root of a number in java' in voice_data:
        reply("To find the square root of a number in Java, you can use the Math.sqrt() method. Here's an example:\n\npublic class SquareRootExample {\n    public static void main(String[] args) {\n        double number = 25;\n        double squareRoot = Math.sqrt(number);\n\n        System.out.println('Square root: ' + squareRoot);\n    }\n}")
    









    
    #python

    elif "top 10 tourist destinations" in voice_data:
        reply("I'm sorry, but I am not able to provide you with a list of top tourist destinations without more specific information or context. Can you please provide me with more details about what type of tourist destination you are looking for?")
    
    elif "what is surrealism" in voice_data:
        reply("Surrealism is a cultural movement that began in the early 1920s, and is best known for its visual artworks and writings. It was a way to express the imagination as revealed in dreams, and to explore the unconscious mind. Would you like me to provide more information?")
   
    elif "build a neural network" in voice_data:
        reply("To build a neural network in Python, you can use libraries such as TensorFlow, Keras, or PyTorch. These libraries provide high-level APIs for building and training neural networks. Would you like me to provide more information?")
   
    elif "best Python library for AI" in voice_data:
        reply("There are several Python libraries available for AI, including TensorFlow, Keras, PyTorch, and scikit-learn. The best library for you will depend on your specific needs and the type of AI project you are working on. Would you like me to provide more information?")

    

    elif 'explain' in voice_data:
        reply('Opening ' + voice_data.split('explain')[1])
        url = 'https://www.perplexity.ai/'
        try:
            webbrowser.get().open(url) 
            reply('type what you want to explain and press Enter')
        except:
            reply('Please check your Internet')
    
    elif 'search' in voice_data:
        reply('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' + voice_data.split('search')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found ')
        except:
            reply('Please check your Internet')
    
    
    elif 'location' in voice_data:
        reply('📍Which place are you looking for?📍')
        temp_audio = record_audio()
        app.eel.addUserMsg(temp_audio)
        reply('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found Atanu')
        except:
            reply('Please check your Internet')
    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        reply('Copied')
          
    elif 'page' in voice_data or 'pest'  in voice_data or 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        reply('Pasted')
        
    elif ('bye' in voice_data) or ('by' in voice_data):
        reply("Good bye Atanu! Have a nice day.")
        is_awake = False

    
   
    # File Navigation (Default Folder set to C://)
    elif 'list' in voice_data:
        counter = 0
        path = 'y://'
        files = listdir(path)
        filestr = ""
        for f in files:
            counter+=1
            print(str(counter) + ':  ' + f)
            filestr += str(counter) + ':  ' + f + '<br>'
        file_exp_status = True
        reply('These are the files in your root directory')
        app.ChatBot.addAppMsg(filestr)
        
    elif file_exp_status == True:
        counter = 0   
        if 'open' in voice_data:
            if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                    files = listdir(path)
                    filestr = ""
                    for f in files:
                        counter+=1
                        filestr += str(counter) + ':  ' + f + '<br>'
                        print(str(counter) + ':  ' + f)
                    reply('Files are listed')
                    app.ChatBot.addAppMsg(filestr)
                    
                except:
                    reply('I do not have permission to access this folder')
                                    
        if 'back' in voice_data:
            filestr = ""
            if path == 'C://':
                reply('Sorry, this is the root directory')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a)
                path += '//'
                files = listdir(path)
                for f in files:
                    counter+=1
                    filestr += str(counter) + ':  ' + f + '<br>'
                    print(str(counter) + ':  ' + f)
                reply('ok')
                app.ChatBot.addAppMsg(filestr)
                   
    else: 
        a = voice_data.lstrip("friday ")
    search_query = a.replace(" ", "+")
    search_url = "https://www.google.com/search?q=" + search_query
    webbrowser.open(search_url)
    reply("For Better Explaination Serching google")
        
          
# ------------------Driver Code--------------------

t1 = Thread(target = app.ChatBot.start)
t1.start()

# Lock main thread until Chatbot has started
while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:
    if app.ChatBot.isUserInput():
        #take input from GUI
        voice_data = app.ChatBot.popUserInput()
    else:
        #take input from Voice
        voice_data = record_audio()

    #process voice_data
    if 'friday' in voice_data:
        try:
            #Handle sys.exit()
            respond(voice_data)
        except SystemExit:
            reply("Exit Successfull")
            break
        except:
            #some other exception got raised
            print("EXCEPTION raised while closing.") 
            break
        


