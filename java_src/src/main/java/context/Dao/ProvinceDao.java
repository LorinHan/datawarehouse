package context.Dao;

import context.Model.City;
import context.Model.Province;

import java.util.List;
import java.util.Map;

public interface ProvinceDao {
    List<Province> getAllProvinces();
    List<City> getMyCities(int id);
    /*
    * 获取所有省份到某个景点的人数统计
    * int id: 景点城市id
    * */
    List<Map<String, Object>> getProvinceCountsByCityId(int id);
    List<Map<String, Object>> getEachCityToSomeplaceCounts(int provinceId, int touristId);
    List<Map<String, Object>> getProvinceToTouristPrice(int provinceId, int touristId, int minPrice, int maxPrice);
}
