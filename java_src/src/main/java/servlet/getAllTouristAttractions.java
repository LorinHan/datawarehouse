package servlet;

import context.Dao.TouristAttractionsDao;
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

@WebServlet("/getAllTouristAttractions")
public class getAllTouristAttractions extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        AnnotationConfigApplicationContext ac = BeanUtil.getAc();
        TouristAttractionsDao touristAttractions = ac.getBean("touristAttractions", TouristAttractionsDao.class);
        List<Map<String, Object>> all = touristAttractions.getAll();
        JSONArray jsonArray = new JSONArray();
        for (Map<String, Object> item : all) {
            jsonArray.put(item);
        }
        response.setContentType("text/json; charset=utf-8");
        response.getWriter().write(jsonArray.toString());
    }
}
