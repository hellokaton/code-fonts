public class Code {
    
    String foo = "王爵的技术小黑屋";

    int bar = 2018;

    boolean areYouReady = "are you ready?".length() > 1;

    public static void main(String[] args) {
        Blade.of()
                .get("/", ctx -> ctx.text("Hello World"))
                .start(Application.class, args);
    }

}