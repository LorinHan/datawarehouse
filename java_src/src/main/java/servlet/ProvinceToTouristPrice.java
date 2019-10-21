package servlet;

import context.Dao.ProvinceDao;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import top.jfunc.json.impl.JSONArray;
import utils.BeanUtil;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.util.Map;

@WebServlet("/provinceToTouristPrice")
public class ProvinceToTouristPrice extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/json; charset=utf-8");
        int provinceId = Integer.parseInt(request.getParameter("provinceId"));
        int touristId = Integer.parseInt(request.getParameter("touristId"));
        int minPrice = Integer.parseInt(request.getParameter("minPrice"));
        int maxPrice = Integer.parseInt(request.getParameter("maxPrice"));
        AnnotationConfigApplicationContext ac = BeanUtil.getAc();
        ProvinceDao province = ac.getBean("province", ProvinceDao.class);
        List<Map<String, Object>> maps = province.getProvinceToTouristPrice(provinceId, touristId, minPrice, maxPrice);
        JSONArray jsonArray = new JSONArray();
        for (Map<String, Object> item : maps) {
            jsonArray.put(item);
        }
        response.getWriter().write(jsonArray.toString());
    }
}
