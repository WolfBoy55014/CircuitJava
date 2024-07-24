public class forkbomb {
   public static void main(String[] args) {
      int[] list = new int[35];

      list[0] = 0;
      list[1] = 1;

      for (int i = 2; i < list.length; i++) {
         System.out.println(list[i - 1] + list[i - 2]);
         list[i] = list[i - 1] + list[i - 2];
      }
   }
}
