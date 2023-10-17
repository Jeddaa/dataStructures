const SearchInsertPosition = (nums, target) => {
  let left = 0;
  let right = nums.length -1
  let mid = right / 2;
  if (target > nums[mid]){
    left = mid;
  }
  while (left <= mid){

  }
}


console.log(SearchInsertPosition([1, 3, 5, 6], 5))
