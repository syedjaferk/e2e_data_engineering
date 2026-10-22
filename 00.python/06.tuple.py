photo = ("Srisankar", "Wijay", "Mohammed", "Sathish")
print(photo, photo[1])
print(dir(photo))


def pass_4_values():
    return 1, 2, 3, {"name": "Jafer"}


response = pass_4_values()
response[3]["age"] = 29
print(response, type(response))
