while True:
    try:
        number = int(input("Enter your favourite number.\n"))
        print(10/number)
        break
    except ValueError:
        print("Make sure you have entered a number.")
    except ZeroDivisionError:
        print("Don't pick zero.")
    except:  # for general exceptions.....not advised
        break
    finally:
        print("loop complete")  # code under the finally keyword is executed no matter what
