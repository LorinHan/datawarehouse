package context.Dao;

import context.Model.City;
import context.Model.Province;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository("province")
public class ProvinceDaoImpl implements ProvinceDao {
    @Autowired
    private JdbcTemplate template;

    @Override
    public List<Province> getAllProvinces() {
        String sql = "select * from provinces;";
        List<Province> query = template.query(sql, new BeanPropertyRowMapper<Province>(Province.class));
        return query;
    }

    @Override
    public List<City> getMyCities(int id) {
        String sql = "select * from cities where province_id = ?;";
        List<City> query = template.query(sql, new BeanPropertyRowMapper<City>(City.class), id);
        return query;
    }

    @Override
    public List<Map<String, Object>> getProvinceCountsByCityId(int id) {
        String sql = "select pro.province, sum(inf.count) as count from (cities ct left join provinces pro on ct.province_id = pro.id) right join infomations inf on inf.from_city_id = ct.id where inf.to_city_id = ? group by pro.province;";
        List<Map<String, Object>> maps = template.queryForList(sql, id);
        return maps;
    }

    @Override
    public List<Map<String, Object>> getEachCityToSomeplaceCounts(int provinceId, int touristId) {
        String sql = "select ct.city, sum(inf.count) as count from infomations inf left join (cities ct left join provinces pro on ct.province_id = pro.id) on inf.from_city_id = ct.id where pro.id = ? and inf.to_city_id = ? group by ct.city;";
        List<Map<String, Object>> maps = template.queryForList(sql, provinceId, touristId);
        return maps;
    }

    @Override
    public List<Map<String, Object>> getProvinceToTouristPrice(int provinceId, int touristId, int minPrice, int maxPrice) {
        String sql = "select sum(inf.count) from infomations inf left join (cities ct left join provinces pro on ct.province_id = pro.id) on inf.from_city_id = ct.id where pro.id = ? and inf.to_city_id = ? and inf.price >= ? and inf.price < ?;";
        List<Map<String, Object>> maps = template.queryForList(sql, provinceId, touristId, minPrice, maxPrice);
        return maps;
    }
}
