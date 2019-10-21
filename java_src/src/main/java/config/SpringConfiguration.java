package config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.context.annotation.Import;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@Configuration
@ComponentScan("context")
@EnableAspectJAutoProxy
@EnableTransactionManagement
@Import({JdbcConfig.class, TransactionConfig.class})
public class SpringConfiguration {
}
