# Insertion Sorting # for i := 1 to size-1 do
key := array[i] j := i
while j > 0 AND array[j-1] > key do array[j] := array[j-1];
j := j – 1 done
array[j] := key


done
# Selection Sort #

for i := 0 to size-2 do //find minimum from ith location to size iMin := i;
for j:= i+1 to size – 1 do
if array[j] < array[iMin] then iMin := j
done
swap array[i] with array[iMin]. done
