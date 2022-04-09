def solution(bridge_length, weight, truck_weights):

    second = 0
    bridge = []
    where = []
    
    while truck_weights or bridge:
        second += 1     
        if bridge:
            where = [x + 1 for x in where]
            if where[0] >= bridge_length:
                where.pop(0)
                bridge.pop(0)

        if truck_weights:            
            if sum(bridge) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)    
                bridge.append(truck)
                where.append(0)
    return second