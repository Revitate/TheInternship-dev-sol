public class prime {

    static int n;
    static boolean[] notPrime;
    
    public static void main(String[] args) {
        int len = args.length;
        if(len < 1){
            System.err.println("please input n!");
            return;
        }else{
            n = Integer.parseInt(args[0]);
            notPrime = new boolean[1000000];

            for(int i=2;i<=n; i++){
                if (!notPrime[i]) {
                    for (int index = i*2; index <= n; index+=i) {
                        notPrime[index] = true;
                    }
                }
            }
            for(int i=2;i<=n;i++) {
                if (!notPrime[i]){
                    System.out.print(i+" ");
                }
            }
        }
    }
}