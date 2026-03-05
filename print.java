import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.chrono.JapaneseChronology;
import java.util.Random;
import java.util.List;
import java.util.ArrayList;

public class print {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(print::createMenuGui);
    }

    private static void createMenuGui() {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {}

        JFrame menu = new JFrame("Escolha uma opção");
        menu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 30, 30));
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setBackground(Color.WHITE);

        JLabel title = new JLabel("Bem‑vindo");
        title.setFont(new Font("SansSerif", Font.BOLD, 20));
        title.setAlignmentX(Component.CENTER_ALIGNMENT);
        title.setBorder(BorderFactory.createEmptyBorder(0, 0, 20, 0));

        JButton ageBtn = new JButton("Descubra sua idade");
        ageBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        ageBtn.setMaximumSize(new Dimension(200, 40));

        JButton diseaseBtn = new JButton("Descubra sua doença");
        diseaseBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        diseaseBtn.setMaximumSize(new Dimension(200, 40));
        diseaseBtn.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 0));

        JButton calcBtn = new JButton("Calculadora");
        calcBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        calcBtn.setMaximumSize(new Dimension(200, 40));
        calcBtn.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 0));

        panel.add(title);
        panel.add(ageBtn);
        panel.add(diseaseBtn);
        panel.add(calcBtn);

        ageBtn.addActionListener(e -> {
            menu.dispose();
            createAgeGui();
        });

        diseaseBtn.addActionListener(e -> {
            menu.dispose();
            createDiseaseGui();
        });

        calcBtn.addActionListener(e -> {
            menu.dispose();
            createCalculatorGui();
        });

        menu.getContentPane().add(panel);
        menu.pack();
        menu.setResizable(false);
        menu.setLocationRelativeTo(null);
        menu.setVisible(true);
    }

    private static void createAgeGui() {
        JFrame frame = new JFrame("Descubra sua idade");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setBackground(Color.WHITE);

        JLabel title = new JLabel("Descubra sua idade!!!");
        title.setFont(new Font("SansSerif", Font.BOLD, 18));
        title.setAlignmentX(Component.CENTER_ALIGNMENT);
        title.setBorder(BorderFactory.createEmptyBorder(0, 0, 15, 0));

        JLabel nameLabel = new JLabel("Nome:");
        nameLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        JTextField nameField = new JTextField(25);
        nameField.setMaximumSize(new Dimension(Integer.MAX_VALUE, nameField.getPreferredSize().height));
    
        JLabel ageLabel = new JLabel("Idade:");
        ageLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        JTextField ageField = new JTextField(5);
        ageField.setMaximumSize(new Dimension(Integer.MAX_VALUE, ageField.getPreferredSize().height));

        JButton submit = new JButton("Enviar");
        submit.setAlignmentX(Component.CENTER_ALIGNMENT);
        submit.setBackground(new Color(0x4CAF50));
        submit.setForeground(Color.WHITE);
        submit.setFocusPainted(false);

        JLabel resultLabel = new JLabel(" ");
        resultLabel.setForeground(Color.RED);
        resultLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        resultLabel.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 0));
        panel.add(Box.createVerticalGlue());
        panel.add(title);
        panel.add(nameLabel);
        panel.add(nameField);
        panel.add(Box.createVerticalStrut(10));
        panel.add(ageLabel);
        panel.add(ageField);
        panel.add(Box.createVerticalStrut(20));
        panel.add(submit);
        panel.add(resultLabel);
        panel.add(Box.createVerticalStrut(20));
        JButton menuBtn = new JButton("Menu Principal");
        menuBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        menuBtn.setMaximumSize(new Dimension(200, 40));
        menuBtn.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 0));
        panel.add(menuBtn);
        menuBtn.addActionListener(e -> {
            frame.dispose();
            createMenuGui();
        });
        panel.add(Box.createVerticalGlue());

        submit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nome = nameField.getText().trim();
                String idade = ageField.getText().trim();
                if (nome.isEmpty() || idade.isEmpty()) {
                    resultLabel.setText("Por favor preencha todos os campos.");
                } else {
                    String result = "ola " + nome + " voce tem " + idade + " anos!";
                    JOptionPane.showMessageDialog(frame, result, "Resultado", JOptionPane.INFORMATION_MESSAGE);
                    resultLabel.setText(" ");
                }
            }
        });

        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(panel, BorderLayout.CENTER);
        frame.pack();
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    private static void createDiseaseGui() {
        JFrame frame = new JFrame("Descubra sua doença");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setBackground(Color.WHITE);

        JLabel title = new JLabel("Selecione seus sintomas");
        title.setFont(new Font("SansSerif", Font.BOLD, 18));
        title.setAlignmentX(Component.CENTER_ALIGNMENT);
        title.setBorder(BorderFactory.createEmptyBorder(0, 0, 15, 0));

        // checkbox list of symptoms
        JCheckBox cbHeadache = new JCheckBox("Dor de cabeça");
        JCheckBox cbFever = new JCheckBox("Febre");
        JCheckBox cbBodyPain = new JCheckBox("Dor no corpo");
        JCheckBox cbStomach = new JCheckBox("Dor de barriga");
        JCheckBox cbTired = new JCheckBox("Cansaço");
        JCheckBox cbOther = new JCheckBox("Outro");
        cbHeadache.setAlignmentX(Component.LEFT_ALIGNMENT);
        cbFever.setAlignmentX(Component.LEFT_ALIGNMENT);
        cbBodyPain.setAlignmentX(Component.LEFT_ALIGNMENT);
        cbStomach.setAlignmentX(Component.LEFT_ALIGNMENT);
        cbTired.setAlignmentX(Component.LEFT_ALIGNMENT);
        cbOther.setAlignmentX(Component.LEFT_ALIGNMENT);

        JButton submit = new JButton("Enviar");
        submit.setAlignmentX(Component.CENTER_ALIGNMENT);
        submit.setBackground(new Color(0xF44336));
        submit.setForeground(Color.WHITE);
        submit.setFocusPainted(false);

        JLabel resultLabel = new JLabel(" ");
        resultLabel.setForeground(Color.BLUE);
        resultLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        resultLabel.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 0));

        panel.add(Box.createVerticalGlue());
        panel.add(title);
        panel.add(cbHeadache);
        panel.add(cbFever);
        panel.add(cbBodyPain);
        panel.add(cbStomach);
        panel.add(cbTired);
        panel.add(cbOther);
        panel.add(Box.createVerticalStrut(20));
        panel.add(submit);
        panel.add(resultLabel);
        // botão de retorno ao menu principal
        panel.add(Box.createVerticalStrut(20));
        JButton menuBtn = new JButton("Menu Principal");
        menuBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        menuBtn.setMaximumSize(new Dimension(200, 40));
        menuBtn.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 0));
        panel.add(menuBtn);
        // volta ao menu principal quando clicado
        menuBtn.addActionListener(e -> {
            frame.dispose();
            createMenuGui();
        });
        panel.add(Box.createVerticalGlue());

        submit.addActionListener(e -> {
            java.util.List<String> symptoms = new java.util.ArrayList<>();
            if (cbHeadache.isSelected()) symptoms.add("Dor de cabeça");
            if (cbFever.isSelected()) symptoms.add("Febre");
            if (cbBodyPain.isSelected()) symptoms.add("Dor no corpo");
            if (cbStomach.isSelected()) symptoms.add("Dor de barriga");
            if (cbTired.isSelected()) symptoms.add("Cansaço");
            if (cbOther.isSelected()) symptoms.add("Outro");

            if (symptoms.isEmpty()) {
                resultLabel.setText("Nenhum sintoma selecionado.");
            } else {
                String joined = String.join(", ", symptoms);
                resultLabel.setText("Sintomas: " + joined);
                JOptionPane.showMessageDialog(frame, "Você tem " + joined,
                        "Resultado", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(panel, BorderLayout.CENTER);
        frame.pack();
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    private static void createCalculatorGui() {
        JFrame frame = new JFrame("Calculadora");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // combobox para tipo de operação
        String[] ops = new String[]{"+","-","*","/"};
        JComboBox<String> opType = new JComboBox<>(ops);

        JPanel buttonPanel = new JPanel(new GridLayout(0, 3, 5, 5));
        Random rand = new Random();

        Runnable regenerate = () -> {
            buttonPanel.removeAll();
            String opChar = (String) opType.getSelectedItem();
            for (int unidades = 0; unidades < 3; unidades ++) {
                // generate only the first operand randomly
                int a = rand.nextInt(100);
                JButton btn = new JButton(String.valueOf(a));
                btn.addActionListener(e -> {
                    // open window with 500 equations and a "Mais" button
                    int fixedA = a;
                    JFrame eqFrame = new JFrame("Escolha uma equação");
                    eqFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                    DefaultListModel<String> model = new DefaultListModel<>();
                    JList<String> list = new JList<>(model);
                    list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

                    Runnable fillModel = () -> {
                        model.clear();
                        for (int i = 0; i < 500; i++) {
                            int b2 = rand.nextInt(100);
                            String op = ops[rand.nextInt(ops.length)];
                            if ("/".equals(op) && b2 == 0) b2 = 1;
                            model.addElement(fixedA + " " + op + " " + b2);
                        }
                    };
                    fillModel.run();

                    JButton chooseBtn = new JButton("Escolher");
                    chooseBtn.addActionListener(ev -> {
                        String sel = list.getSelectedValue();
                        if (sel != null) {
                            String[] parts = sel.split(" ");
                            int x = Integer.parseInt(parts[0]);
                            int y = Integer.parseInt(parts[2]);
                            String op = parts[1];
                            String res;
                            switch (op) {
                                case "+": res = String.valueOf(x + y); break;
                                case "-": res = String.valueOf(x - y); break;
                                case "*": res = String.valueOf(x * y); break;
                                default:
                                    res = String.format("%.4f", y == 0 ? 0.0 : ((double)x / y));
                            }
                            JOptionPane.showMessageDialog(eqFrame, res, "Resultado", JOptionPane.INFORMATION_MESSAGE);
                        }
                    });
                    JButton moreBtn = new JButton("Mais");
                    moreBtn.addActionListener(ev -> fillModel.run());

                    JPanel bottom = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
                    bottom.add(chooseBtn);
                    bottom.add(moreBtn);

                    eqFrame.getContentPane().add(new JScrollPane(list), BorderLayout.CENTER);
                    eqFrame.getContentPane().add(bottom, BorderLayout.SOUTH);
                    eqFrame.setSize(400, 500);
                    eqFrame.setLocationRelativeTo(frame);
                    eqFrame.setVisible(true);
                });
                buttonPanel.add(btn);
            }
            buttonPanel.revalidate();
            buttonPanel.repaint();
        };

        opType.addActionListener(e -> regenerate.run());
        regenerate.run();

        JButton regenerateBtn = new JButton("Gerar novas operações");
        regenerateBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        regenerateBtn.addActionListener(e -> regenerate.run());

        JButton menuBtn = new JButton("Menu Principal");
        menuBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        menuBtn.addActionListener(e -> {
            frame.dispose();
            createMenuGui();
        });

        JPanel topPanel = new JPanel();
        topPanel.add(new JLabel("Operação: ")); topPanel.add(opType);

        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        bottomPanel.add(regenerateBtn);
        bottomPanel.add(menuBtn);

        frame.getContentPane().add(topPanel, BorderLayout.NORTH);
        frame.getContentPane().add(new JScrollPane(buttonPanel), BorderLayout.CENTER);
        frame.getContentPane().add(bottomPanel, BorderLayout.SOUTH);
        frame.pack();
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}