package servlet;

import context.Dao.ProvinceDao;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import top.jfunc.json.impl.JSONArray;
import top.jfunc.json.impl.JSONObject;
import utils.BeanUtil;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.util.Map;

@WebServlet("/getProvinceCountsByCityId")
public class getProvinceCountsBycityId extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/json; charset=utf-8");
        int cityId = Integer.parseInt(request.getParameter("cityId"));
        AnnotationConfigApplicationContext ac = BeanUtil.getAc();
        ProvinceDao province = ac.getBean("province", ProvinceDao.class);
        List<Map<String, Object>> resMap = province.getProvinceCountsByCityId(cityId);
        JSONArray jsonArray = new JSONArray();
        for (Map<String, Object> item : resMap) {
            jsonArray.put(item);
        }
        response.getWriter().write(jsonArray.toString());
    }
}
