package context;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository("testDruid")
public class TestDruidImpl implements TestDruid {
    @Autowired
    private JdbcTemplate template;
    public void testAll() {
        System.out.println(template);
        List<Map<String, Object>> maps = template.queryForList("select * from provinces;");
        for(Object item: maps) {
            System.out.println(item);
        }
    }
}
