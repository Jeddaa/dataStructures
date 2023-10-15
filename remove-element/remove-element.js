const RemoveElement = (nums, val) => {
  let j = 0;
  for (let i=0;i<nums.length;i++){
    if(nums[i] != val){
      nums[j] = nums[i];
      j++;
    }
  }
  console.log(nums);
  return j;
}


console.log(RemoveElement([0, 1, 2, 2, 3, 0, 4, 2], 2));
