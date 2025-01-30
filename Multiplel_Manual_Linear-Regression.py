#Hi, to understand what's happening in this code, check out my repository on linear regression, where everything is explained in detail.
#  Here, I'm doing the same process but manually.

import numpy as np

import time

import sys

import threading

build_area =np.array([130,130,130,130,130,130,130,130,130,130,
    130,130,130,130,130,130,130,130,130,130,

  130,130,130,130,130,140,140,140,140,140,
  140,140,140,140,140,140,140,140,140,140,

  140,140,140,140,140,150,150,150,150,150,
  150,150,150,150,150,150,150,150,150,150,
 
  150,150,150,150,150,160,160,160,160,160,
  160,160,160,160,160,160,160,160,160,160,
  
  160,160,160,160,160,160,160,160,160,160,
  160,160,160,160,160,160,160,160,160,160,
  
  170,170,170,170,170,170,170,170,170,170,
  170,170,170,170,170,170,170,170,170,170,
  
  170,170,170,170,170,180,180,180,180,180,
  180,180,180,180,180,180,180,180,180,180,
  
  180,180,180,180,180,180,180,180,180,180,
  190,190,190,190,190,190,190,190,190,190,
  
  190,190,190,190,190,190,190,190,190,190,
  190,190,190,190,190,200,200,200,200,200,
  
  200,200,200,200,200,200,200,200,200,200,
  200,200,200,200,200,200,200,200,200,200,
  
  210,210,210,210,210,210,210,210,210,210,
  210,210,210,210,210,210,210,210,210,210,
  
  210,210,210,210,210,220,220,220,220,220,
  220,220,220,220,220,220,220,220,220,220,
  
  220,220,220,220,220,220,220,220,220,220,
  230,230,230,230,230,230,230,230,230,230,
  
  230,230,230,230,230,230,230,230,230,230,
  230,230,230,230,230,240,240,240,240,240,
  
  240,240,240,240,240,240,240,240,240,240,
  240,240,240,240,240,240,240,240,240,240,
  
  250,250,250,250,250,250,250,250,250,250,
  250,250,250,250,250,250,250,250,250,250,
  
  250,250,250,250,250,260,260,260,260,260,
  260,260,260,260,260,260,260,260,260,260,
  
  260,260,260,260,260,260,260,260,260,260,
  270,270,270,270,270,270,270,270,270,270,
  
  270,270,270,270,270,270,270,270,270,270,
  270,270,270,270,270,280,280,280,280,280,
  
  280,280,280,280,280,280,280,280,280,280,
  280,280,280,280,280,280,280,280,280,280,])

build_age =np.array([ 1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,
            
             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,])

build_room = np.array([ 2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,])

build_price =np.array([207000,212000,217000,222000,227000,209000,214000,219000,224000,229000,
  211000,216000,221000,226000,231000,213000,218000,223000,228000,233000,

  215000,220000,225000,230000,235000,222000,227000,232000,237000,242000,
  224000,229000,234000,239000,244000,226000,231000,236000,241000,246000,

  228000,233000,238000,243000,248000,230000,235000,240000,245000,250000,
  237000,242000,247000,252000,257000,239000,244000,249000,254000,259000,

  241000,246000,251000,256000,261000,243000,248000,253000,258000,263000,
  245000,250000,255000,260000,265000,252000,257000,262000,267000,272000,

  254000,259000,264000,269000,274000,256000,261000,266000,271000,276000,
  258000,263000,268000,273000,278000,260000,265000,270000,275000,280000,

  267000,272000,277000,282000,287000,269000,274000,279000,284000,289000,
  271000,276000,281000,286000,291000,273000,278000,283000,288000,293000,

  275000,280000,285000,290000,295000,282000,287000,292000,297000,302000,
  284000,289000,294000,299000,304000,286000,291000,296000,301000,306000,

  288000,293000,298000,303000,308000,290000,295000,300000,305000,310000,
  297000,302000,307000,312000,317000,299000,304000,309000,314000,319000,

  301000,306000,311000,316000,321000,303000,308000,313000,318000,323000,
  305000,310000,315000,320000,325000,312000,317000,322000,327000,332000,

  314000,319000,324000,329000,334000,316000,321000,326000,331000,336000,
  318000,323000,328000,333000,338000,320000,325000,330000,335000,340000,

  327000,332000,337000,342000,347000,329000,334000,339000,344000,349000,
  331000,336000,341000,346000,351000,333000,338000,343000,348000,353000,

  335000,340000,345000,350000,355000,342000,347000,352000,357000,362000,
  344000,349000,354000,359000,364000,346000,351000,356000,361000,366000,

  348000,353000,358000,363000,368000,350000,355000,360000,365000,370000,
  357000,362000,367000,372000,377000,359000,364000,369000,374000,379000,

  361000,366000,371000,376000,381000,363000,368000,373000,378000,383000,
  365000,370000,375000,380000,385000,372000,377000,382000,387000,392000,

  374000,379000,384000,389000,394000,376000,381000,386000,391000,396000,
  378000,383000,388000,393000,398000,380000,385000,390000,395000,400000,

  387000,392000,397000,402000,407000,389000,394000,399000,404000,409000,
  391000,396000,401000,406000,411000,393000,398000,403000,408000,413000,

  395000,400000,405000,410000,415000,402000,407000,412000,417000,422000,
  404000,409000,414000,419000,424000,406000,411000,416000,421000,426000,

  408000,413000,418000,423000,428000,410000,415000,420000,425000,430000,
  417000,422000,427000,432000,437000,419000,424000,429000,434000,439000,

  421000,426000,431000,436000,441000,423000,428000,433000,438000,443000,
  425000,430000,435000,440000,445000,432000,437000,442000,447000,452000,

  434000,439000,444000,449000,454000,436000,441000,446000,451000,456000,
  438000,443000,448000,453000,458000,440000,445000,450000,455000,460000,])

build_area_test = np.array([290,290,290,290,290,290,290,290,290,290,
  290,290,290,290,290,290,290,290,290,290,
  
  290,290,290,290,290,300,300,300,300,300,
  300,300,300,300,300,300,300,300,300,300,
  
  300,300,300,300,300,300,300,300,300,300,
  310,310,310,310,310,310,310,310,310,310,
  
  310,310,310,310,310,310,310,310,310,310,
  310,310,310,310,310,320,320,320,320,320,
  
  320,320,320,320,320,320,320,320,320,320,
  320,320,320,320,320,320,320,320,320,320])

build_age_test = np.array([ 1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5,

             1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5])

build_room_test = np.array([ 2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6,

  2,3,4,5,6,2,3,4,5,6,
  2,3,4,5,6,2,3,4,5,6])

build_price_test = np.array([447000,452000,457000,462000,467000,449000,454000,459000,464000,469000,
  451000,456000,461000,466000,471000,453000,458000,463000,468000,473000,

  455000,460000,465000,470000,475000,462000,467000,472000,477000,482000,
  464000,469000,474000,479000,484000,466000,471000,476000,481000,486000,

  468000,473000,478000,483000,488000,470000,475000,480000,485000,490000,
  477000,482000,487000,492000,497000,479000,484000,489000,494000,499000,

  481000,486000,491000,496000,501000,483000,488000,493000,498000,503000,
  485000,490000,495000,500000,505000,492000,497000,502000,507000,512000,

  494000,499000,504000,509000,514000,496000,501000,506000,511000,516000,
  498000,503000,508000,513000,518000,500000,505000,510000,515000,520000])


def load_anim(stop_event):
    
    while not stop_event.is_set():
            
            for dots in range(4):

                sys.stdout.write("\rThis may take a few seconds" + "." * dots)  
                
                sys.stdout.flush()  
                
                time.sleep(0.5) 
                
                if stop_event.is_set():
                
                    break


def normal_equation (build_features ,build_price):

    x = build_features

    y = build_price

    x_transpose = x.T 

    x_transpose_x = x_transpose.dot(x)

    x_transpose_x_inv = np.linalg.inv(x_transpose_x)

    x_transpose_y = x_transpose.dot(y)

    weight = x_transpose_x_inv.dot(x_transpose_y)

    return(weight)

def mean_value(values):

    total_sum =sum(values)

    count =len(values)

    mean_value = total_sum / count

    return (mean_value)


def gradient_descent(build_features , build_price , learning_rate = 0.00001 , iter = 100000):

    m , n = build_features.shape

    b = np.zeros(n + 1)

    for _ in range(iter):

        build_price_predicted_gradient = b[0] + np.dot(build_features , b[1:])

        errors = build_price - build_price_predicted_gradient

        b0_array = []

        b_array = np.zeros(n)

        for index in range (len(errors)):

            b0_array.append(-2 * errors[index])

            for j in range(n):
                b_array[j] = b_array[j] + (-2 * errors[index] * build_features[index][j])

        b0_array_mean = mean_value(b0_array)

        b_array_mean = b_array / m

        b[0] -= learning_rate * b0_array_mean

        b[1:] -= learning_rate * b_array_mean

    return b



def mse_calc(build_price_test , build_price_predicted):

    mse_array = []

    for index in range (len(build_price_test)):

        error = (build_price_test[index] - build_price_predicted[index]) ** 2

        mse_array.append(error)

    mse = mean_value(mse_array)

    return(mse)




def r2_calc(build_price_test , build_price_predicted):

    rss = 0.0

    tss = 0.0

    for index in range (len(build_price_test)):

        rss += (build_price_test[index] - build_price_predicted[index]) ** 2

        tss += (build_price_test[index] - mean_value(build_price_test)) ** 2

    if tss == 0 :
        r2_score = 1.0

    else :

        r2_score = 1 - (rss / tss)

    return (r2_score)




def mae_calc (build_price_test, build_price_predicted):

    mae_array = []

    for index in range (len(build_price_test)):

        error = abs(build_price_test[index] - build_price_predicted[index])

        mae_array.append(error)

    mae = mean_value(mae_array)
    
    return(mae)



choice = int(input("Choose a method to solve this: (1) Normal Equation or (2) Gradient Descent: "))

if choice == 1: 

    print("Provide detailed information about the building, keeping in mind that the building will be considered as located in Abdoun, Amman, Jordan..")
    
    area_input = [int(input("Add the size of the building in m^2: "))]

    age_input = [int(input("Add the age of the building: "))]

    room_input = [int(input("Add how many rooms in the building: "))]

    build_features_normal_equation = np.column_stack((np.ones(len(build_area)) ,build_area, build_age, build_room))


    weights = normal_equation(build_features_normal_equation , build_price)


    build_features_test = np.column_stack((np.ones(len(build_area_test)) , build_area_test , build_age_test , build_room_test))


    build_price_predicted_ori = build_features_test.dot(weights)

    build_features_input = np.column_stack((np.ones(len(area_input)) , area_input , age_input , room_input))

    build_price_predicted = build_features_input.dot(weights)

    y_pred_int = int(build_price_predicted[0])

    y_pred_number = f"{y_pred_int:,}"

    print("The expected price in JD is :",y_pred_number,"JD")

    print("The mean Squared Error is: ", mse_calc(build_price_test , build_price_predicted_ori))

    print("The R^2 Score is: ", r2_calc(build_price_test , build_price_predicted_ori))

    print("The Mean Absolute Error is: ", mae_calc(build_price_test , build_price_predicted_ori))



elif choice == 2:

    print("Provide detailed information about the building, keeping in mind that the building will be considered as located in Abdoun, Amman, Jordan..")

    area_input = [int(input("Add the size of the building in m^2: "))]

    age_input = [int(input("Add the age of the building: "))]

    room_input = [int(input("Add how many rooms in the building: "))]

    stop_event = threading.Event()

    anim_thread = threading.Thread(target=load_anim , args = (stop_event,))

    anim_thread.start()


    build_features_gradient_descent = np.column_stack((build_area ,build_age , build_room))


    b = gradient_descent(build_features_gradient_descent , build_price , learning_rate = 0.00001 , iter = 100000)


    build_features_test2 = np.column_stack((np.ones(len(build_area_test)) , build_area_test ,build_age_test , build_room_test))


    build_price_predicted2_ori = build_features_test2.dot(b)


    build_features_input = np.column_stack((np.ones(len(area_input)) , area_input , age_input , room_input))

    build_price_predicted2 = build_features_input.dot(b)

    y_pred_int = int(build_price_predicted2[0])

    y_pred_number = f"{y_pred_int:,}"

    print("The expected price in JD is :",y_pred_number,"JD")

    print("The mean Squared Error is: ", mse_calc(build_price_test , build_price_predicted2_ori))

    print("The R^2 Score is: ", r2_calc(build_price_test , build_price_predicted2_ori))

    print("The Mean Absolute Error is: ", mae_calc(build_price_test , build_price_predicted2_ori))

    stop_event.set()

    anim_thread.join()

    sys.stdout.write("\rThis may take a few seconds... Done!\n")

else :

    print("Write a valid number!!")