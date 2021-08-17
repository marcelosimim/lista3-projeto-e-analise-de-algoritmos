from array_generator import *
from auxiliary_methods import print_results
from sort_methods import *

n = 100
#n = 1000
#n = 10000
#n = 1000000

algorithm = 'SELECTION'

print(f'========== N = {n} ==========\n\n')

comparisons, movements, time_seconds = select(ordered_array(n))
print_results(
    f'ORDENADO - {algorithm}', comparisons, movements, time_seconds)

comparisons, movements, time_seconds = select(disordered_array(n))
print_results(
    f'DESORDENADO - {algorithm}', comparisons, movements, time_seconds)

comparisons, movements, time_seconds = select(random_array(n))
print_results(
    f'ALEATORIO - {algorithm}', comparisons, movements, time_seconds)

comparisons, movements, time_seconds = select(partially_random_array(n))
print_results(
    f'PARCIALMENTE ALEATORIO - {algorithm}', comparisons, movements, time_seconds)
