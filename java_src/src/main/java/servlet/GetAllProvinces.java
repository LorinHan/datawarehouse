package servlet;

import config.SpringConfiguration;
import context.Dao.ProvinceDao;
import context.Model.Province;
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

@WebServlet("/getAllProvinces")
public class GetAllProvinces extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/json; charset=utf-8");
        AnnotationConfigApplicationContext ac = BeanUtil.getAc();
        ProvinceDao province = ac.getBean("province", ProvinceDao.class);
        List<Province> allProvinces = province.getAllProvinces();
        JSONArray jsonArray = new JSONArray();
        for (Province item : allProvinces) {
            jsonArray.put(item);
        }
        response.getWriter().println(jsonArray);
    }
}
