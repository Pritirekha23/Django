from django.shortcuts import render,HttpResponse
from .forms import CalculatorForm

def Calculator_view(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['symbol']

            if operation == '+':
                operation_name = 'Addition'
                result = num1 + num2
            elif operation == '-':
                operation_name = 'substraction'
                result = num1 - num2
            elif operation == '*':
                operation_name = 'multiplication'
                result = num1 * num2
            elif operation == '/':
                 operation_name = 'division'
                 if num2 != 0:
                    result = num1 / num2
                 else:
                    result = 'It Cannot divided by zero'
            else:
                return HttpResponse('Invalid operation')

            d = {
                'num1': num1,
                'num2': num2,
                'operation_name': operation_name,
                'result': result
            }
            return render(request, 'CalculatorApp/result.html',d)
    else:
        form = CalculatorForm()
        d={'form':form}

    return render(request, 'CalculatorApp/home.html', d)
