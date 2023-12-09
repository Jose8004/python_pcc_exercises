def merge_and_sort_lists(list1, list2):
    x = list1.extend(list2)
    return sorted(x)

print(merge_and_sort_lists([1, 2, 3], [4, 5, 9]))

#            string = f"{self.registered_vehicles.keys().title()}: {self.registered_vehicles.values().title()}-{self.registered_vehicles.values().title()}"
#            list.append(string)
#            return string