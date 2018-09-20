for x in xrange(3):
    for y in xrange(3):
        for z in xrange(3):
            print x, y, z
            if x * y * z == 3:
                break
        else:
            continue
        break
    else:
        continue
    break




# for x in xrange(10):
#     for y in xrange(10):
#         for z in xrange(10):
#             print x, y, z
#             if x+y+z==3:
#                 break