package context.Dao;

import java.util.List;
import java.util.Map;

public interface TouristAttractionsDao {
    List<Map<String, Object>> getAll();
    List<Map<String, Object>> getCountsGroupByEach();
    List<Map<String, Object>> getCountsGroupByArea();
}
