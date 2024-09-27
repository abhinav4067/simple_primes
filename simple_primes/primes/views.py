from django.shortcuts import render



def input_page(request):
    return render(request, 'primes/input_page.html')

def prime_output(request):
    if request.method == 'POST':
        number = int(request.POST.get('number'))

        # check prime logic
        primes = []
        for i in range(2, number + 1):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)

        return render(request, 'primes/output_page.html', {'primes': primes, 'number': number})
    
    return render(request, 'primes/input_page.html')