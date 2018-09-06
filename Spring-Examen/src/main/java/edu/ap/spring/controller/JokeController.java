package edu.ap.spring.controller;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLDecoder;

import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@Scope("session")
public class JokeController {
   
   public JokeController() {
   }
       
   @RequestMapping("/joke")
   public String joke(@RequestParam("firstname") String firstName, @RequestParam("lastname") String lastName, Model model) {
	   String jokeUrl = "http://api.icndb.com/jokes/random?firstname=" + firstName + "&lastname=" + lastName;
	   String inputLine;
	   
	   return "";
   }
		   
   @RequestMapping("/joke_post")
   public String joke_post() {
	   return "";
   }
   
   @RequestMapping("/")
   public String root() {
	   return "redirect:/joke";
   }
}
