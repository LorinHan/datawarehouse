package context.Dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository("touristAttractions")
public class TouristAttractionsImpl implements TouristAttractionsDao {
    @Autowired
    JdbcTemplate template;

    @Override
    public List<Map<String, Object>> getAll() {
        String sql = "select tourist_attractions.*, cities.city, provinces.province from tourist_attractions left join (cities left join provinces on cities.province_id = provinces.id) on tourist_attractions.city_id = cities.id and tourist_attractions.province_id = provinces.id;";
        List<Map<String, Object>> maps = template.queryForList(sql);
        return maps;
    }

    @Override
    public List<Map<String, Object>> getCountsGroupByEach() {
        String sql = "select sum(inf.count) as count, ct.city from infomations inf right join (tourist_attractions ta left join cities ct on ta.city_id = ct.id) on inf.to_city_id = ta.city_id group by ta.city_id;";
        List<Map<String, Object>> maps = template.queryForList(sql);
        return maps;
    }

    @Override
    public List<Map<String, Object>> getCountsGroupByArea() {
        String sql = "select sum(inf.count) as count, ta.area from infomations inf right join (tourist_attractions ta left join cities ct on ta.city_id = ct.id) on inf.to_city_id = ta.city_id group by ta.area;";
        List<Map<String, Object>> maps = template.queryForList(sql);
        return maps;
    }
}
