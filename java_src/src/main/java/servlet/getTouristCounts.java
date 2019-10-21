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

@WebServlet("/getTouristCounts")
public class getTouristCounts extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/json; charset=utf-8");
        String groupBy = request.getParameter("groupBy");
        AnnotationConfigApplicationContext ac = BeanUtil.getAc();
        TouristAttractionsDao touristAttractions = ac.getBean("touristAttractions", TouristAttractionsDao.class);
        List<Map<String, Object>> maps = null;
        JSONArray jsonArray = new JSONArray();
        if(groupBy.equals("each")) {
            maps = touristAttractions.getCountsGroupByEach();
        } else if(groupBy.equals("area")) {
            maps = touristAttractions.getCountsGroupByArea();
        } else {
            response.getWriter().write("Err Request");
        }
        if(maps != null) {
            for (Map<String, Object> item : maps) {
                jsonArray.put(item);
            }
        }
        response.getWriter().write(jsonArray.toString());
    }
}
