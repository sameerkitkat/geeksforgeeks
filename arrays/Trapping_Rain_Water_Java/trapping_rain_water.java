class TrappingWater {

	public static void main(String[] args){
		int[] arr = {3,0,1,2,5};
		int res = 0;
		for (int i=1;i<arr.length;i++){
			int left = arr[i];
			for (int j=0;j<i;j++){
				left = Math.max(left,arr[j]);
			}
			int right = arr[i];
			for (int j=i+1;j<arr.length;j++){
				right = Math.max(right,arr[j]);
			}
			res=res+(Math.min(left,right)-arr[i]);
		}
		System.out.println("Trapped water is "+res);
	}
}
