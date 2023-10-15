const RemoveDuplicates = (nums) => {
  let j =1;
  for(let i =1; i<nums.length;i++)
  {
    if(nums[i] != nums[i-1]){
      nums[j] = nums[i];
      j++;
    }
  }
  console.log(nums)
  return j;
}
//trying out the function
console.log(RemoveDuplicates([1,1,2,3,4,4,5,6,6,7,8,9,9,10]))
