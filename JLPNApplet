import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class JNLPApplet extends Application {

    @Override
    public void start(Stage primaryStage) {
        TextField urlField = new TextField();
        urlField.setPromptText("Enter JNLP URL");

        Button launchButton = new Button("Launch");
        launchButton.setOnAction(event -> {
            String url = urlField.getText();
            if (url.isEmpty()) {
                System.out.println("Please enter a URL");
                return;
            }

            try {
                URI uri = new URI(url);
                Desktop.getDesktop().browse(uri);
            } catch (URISyntaxException | IOException ex) {
                System.out.println("Error launching JNLP: " + ex.getMessage());
            }
        });

        VBox root = new VBox(10);
        root.getChildren().addAll(urlField, launchButton);
        root.setAlignment(Pos.CENTER);
        root.setPadding(new Insets(10));

        Scene scene = new Scene(root, 300, 100);
        primaryStage.setScene(scene);
        primaryStage.setTitle("JNLP Applet");
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}