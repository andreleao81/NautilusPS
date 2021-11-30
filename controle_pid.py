'''
"PID de uma gangorra -- Capacitação 2022"

"Nota: neste entregável você terá que implementar um controle PID simples, de uma dimensão, após 10 loops."

#Constantes PID --> Kp = 3 ; Ki = 1 ; Kd = 0.1 || Outputs: saída do PID para erro = 30, após 10 loops

'''

setpoint = 0
error = 30
deriv_error, integral_error = 30, 30
past_errors = list()
maximum = 10
setpoint = int()
print(setpoint)
pos = setpoint + 30 

while len(past_errors) < 10:
    
    pid = 3 * error + 1 * deriv_error + 0.1 * integral_error
    past_error = error
    error = setpoint - pid
    past_errors.append(past_error)
    erro_integral = sum(past_errors) + error    
    deriv_error = error - past_error



'''
"PID de uma gangorra -- Capacitação 2022"

"Nota: neste entregável você terá que implementar um controle PID simples, de uma dimensão, após 10 loops."

Constantes PID --> Kp = 3 ; Ki = 1 ; Kd = 0.1 || Outputs: saída do PID para erro = 30, após 10 loops

pid formula : pid = kp * error + kd * deriv_error + ki * integral_error
'''

past_all  =  list()
error,  deriv_error,  integral_error  =  30,  0,   0
kp,  ki,  kd  = 3,  1,  0.1


for i in range(10):
    pid = kp * error + kd * deriv_error + ki * integral_error
    print(pid)
    past_error = error
    deriv_error = error - past_error
    past_all.append(past_error)
    integral_error = error + sum(past_all)

print(f'\n\nPID after 10 loops: {pid}')



# print(f'Depois de {maximum} loops, a saida do PID para erro = 30 é de : {pid}')
print(pid)