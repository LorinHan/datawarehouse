package utils;

import config.SpringConfiguration;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class BeanUtil {

    private static AnnotationConfigApplicationContext ac;
    static {
        ac = new AnnotationConfigApplicationContext(SpringConfiguration.class);
    }
    public static AnnotationConfigApplicationContext getAc() {
        return ac;
    }
}
