import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.SimpleDateFormat;
import java.util.Stack;
import java.util.Date;

public class AnfiteatroGUI extends JFrame {
    
    // Matriz de asientos: 10 filas x 10 columnas
    private char[][] asientos;
    private JButton[][] botonesAsientos;
    private JTextArea areaEstado;
    
    // Historial de reservas para la función Deshacer
    private Stack<int[]> historialReservas;
    
    public AnfiteatroGUI() {
        // Inicializar todos los asientos como libres ('L')
        asientos = new char[10][10];
        botonesAsientos = new JButton[10][10];
        historialReservas = new Stack<int[]>();
        
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                asientos[i][j] = 'L';
            }
        }
        
        // Configurar la ventana principal
        setTitle("Sistema de Reserva de Asientos - Anfiteatro");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        setSize(1200, 600);
        setLocationRelativeTo(null);
        setResizable(false); 
        
        // Panel superior con información
        JPanel panelSuperior = new JPanel();
        panelSuperior.setLayout(new BorderLayout());
        panelSuperior.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        JLabel titulo = new JLabel("ANFITEATRO - 10 FILAS x 10 ASIENTOS", SwingConstants.CENTER);
        titulo.setFont(new Font("Arial", Font.BOLD, 20));
        panelSuperior.add(titulo, BorderLayout.NORTH);
        
        // Leyenda de colores
        JPanel leyenda = new JPanel();
        leyenda.setLayout(new FlowLayout());
        
        JLabel verde = new JLabel("  ");
        verde.setOpaque(true);
        verde.setBackground(Color.GREEN);
        verde.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        leyenda.add(verde);
        leyenda.add(new JLabel("= Libre (L)   "));
        
        JLabel rojo = new JLabel("  ");
        rojo.setOpaque(true);
        rojo.setBackground(Color.RED);
        rojo.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        leyenda.add(rojo);
        leyenda.add(new JLabel("= Ocupado (X)"));
        
        panelSuperior.add(leyenda, BorderLayout.CENTER);
        
        // ========== PANEL PRINCIPAL (Centro) ==========
        JPanel panelCentro = new JPanel(new BorderLayout());
        
        // Panel de asientos (izquierda)
        JPanel panelAsientos = new JPanel();
        panelAsientos.setLayout(new GridLayout(10, 10, 5, 5));
        panelAsientos.setBorder(BorderFactory.createTitledBorder("MAPA DE ASIENTOS"));
        
        // Crear botones para cada asiento
        for (int fila = 0; fila < 10; fila++) {
            for (int columna = 0; columna < 10; columna++) {
                JButton boton = new JButton("F" + (fila + 1) + " A" + (columna + 1));
                boton.setBackground(Color.GREEN);
                boton.setOpaque(true);
                boton.setBorderPainted(false);
                boton.setFont(new Font("Arial", Font.BOLD, 10));
                boton.setPreferredSize(new Dimension(70, 20));
                
                final int f = fila;
                final int c = columna;
                
                boton.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        reservarAsiento(f, c);
                    }
                });
                
                botonesAsientos[fila][columna] = boton;
                panelAsientos.add(boton);
            }
        }
        
        // ========== ÁREA DE ESTADO (derecha) ==========
        JPanel panelEstado = new JPanel(new BorderLayout());
        panelEstado.setBorder(BorderFactory.createTitledBorder("ESTADO DEL SISTEMA"));
        panelEstado.setPreferredSize(new Dimension(450, 0));
        
        areaEstado = new JTextArea();
        areaEstado.setEditable(false);
        areaEstado.setFont(new Font("Monospaced", Font.PLAIN, 11));
        areaEstado.setBackground(Color.BLACK);
        areaEstado.setForeground(Color.GREEN);
        areaEstado.setCaretColor(Color.WHITE);
        
        JScrollPane scrollEstado = new JScrollPane(areaEstado);
        scrollEstado.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        panelEstado.add(scrollEstado, BorderLayout.CENTER);
        
        // Panel para botones de acción dentro del área de estado
        JPanel panelBotonesAccion = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        panelBotonesAccion.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JButton btnDeshacer = new JButton("DESHACER ULTIMA RESERVA");
        btnDeshacer.setFont(new Font("Arial", Font.BOLD, 10));
        btnDeshacer.setBackground(Color.YELLOW);
        btnDeshacer.setForeground(Color.BLACK);
        btnDeshacer.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                deshacerReserva();
            }
        });

        JButton btnReiniciar = new JButton("REINICIAR SISTEMA");
        btnReiniciar.setFont(new Font("Arial", Font.BOLD, 10));
        btnReiniciar.setBackground(Color.ORANGE);
        btnReiniciar.setForeground(Color.BLACK);
        btnReiniciar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                reiniciarSistema();
            }
        });

        panelBotonesAccion.add(btnDeshacer);
        panelBotonesAccion.add(btnReiniciar);
        panelEstado.add(panelBotonesAccion, BorderLayout.SOUTH);
        
        // Agregar asientos (izquierda) y estado (derecha) al panel centro
        panelCentro.add(panelAsientos, BorderLayout.CENTER);
        panelCentro.add(panelEstado, BorderLayout.EAST);
               
        // Ensamblar todo
        add(panelSuperior, BorderLayout.NORTH);
        add(panelCentro, BorderLayout.CENTER);
        
        // Mensaje inicial
        agregarEstado("=== SISTEMA DE RESERVA DE ASIENTOS ===");
        agregarEstado("");  
        agregarEstado("INSTRUCCIONES:");
        agregarEstado("- Haga clic en cualquier asiento VERDE para reservarlo");
        agregarEstado("- Use DESHACER para cancelar la ultima reserva");
        agregarEstado("");
    }
    
    private void generarTicket(int fila, int columna) {
        // Crear la ventana del ticket
        JDialog dialogTicket = new JDialog(this, "TICKET DE RESERVA", true);
        dialogTicket.setLayout(new BorderLayout());
        dialogTicket.setSize(400, 500);
        dialogTicket.setLocationRelativeTo(this);
        dialogTicket.setResizable(false);
        
        // Panel principal con borde
        JPanel panelTicket = new JPanel();
        panelTicket.setLayout(new BorderLayout());
        panelTicket.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panelTicket.setBackground(Color.WHITE);
        
        // Título del ticket
        JLabel titulo = new JLabel("ANFITEATRO - TICKET DE RESERVA", SwingConstants.CENTER);
        titulo.setFont(new Font("Arial", Font.BOLD, 16));
        titulo.setForeground(new Color(0, 100, 0));
        titulo.setBorder(BorderFactory.createEmptyBorder(0, 0, 20, 0));
        panelTicket.add(titulo, BorderLayout.NORTH);
        
        // Panel de información
        JPanel panelInfo = new JPanel(new GridLayout(6, 2, 10, 15));
        panelInfo.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panelInfo.setBackground(Color.WHITE);
        
        // Fecha y hora actual
        Date ahora = new Date();
        SimpleDateFormat sdfFecha = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat sdfHora = new SimpleDateFormat("HH:mm:ss");
        
        // Agregar información al panel
        panelInfo.add(crearLabelNegrita("Número de Ticket:"));
        panelInfo.add(crearLabel("T-" + System.currentTimeMillis()));
        
        panelInfo.add(crearLabelNegrita("Fila:"));
        panelInfo.add(crearLabel(String.valueOf(fila + 1)));
        
        panelInfo.add(crearLabelNegrita("Asiento:"));
        panelInfo.add(crearLabel(String.valueOf(columna + 1)));
        
        panelInfo.add(crearLabelNegrita("Ubicación:"));
        panelInfo.add(crearLabel("Fila " + (fila + 1) + ", Asiento " + (columna + 1)));
        
        panelInfo.add(crearLabelNegrita("Fecha:"));
        panelInfo.add(crearLabel(sdfFecha.format(ahora)));
        
        panelInfo.add(crearLabelNegrita("Hora:"));
        panelInfo.add(crearLabel(sdfHora.format(ahora)));
        
        panelTicket.add(panelInfo, BorderLayout.CENTER);
        
        // Línea decorativa
        JSeparator separador = new JSeparator();
        separador.setForeground(Color.BLACK);
        panelTicket.add(separador, BorderLayout.SOUTH);
        
        // Panel de mensaje adicional
        JPanel panelMensaje = new JPanel();
        panelMensaje.setBackground(Color.WHITE);
        JLabel mensaje = new JLabel("✓ Reserva confirmada. ¡Disfrute del espectáculo!");
        mensaje.setFont(new Font("Arial", Font.ITALIC, 11));
        mensaje.setForeground(Color.GRAY);
        panelMensaje.add(mensaje);
        
        // Botón cerrar
        JButton btnCerrar = new JButton("CERRAR");
        btnCerrar.setFont(new Font("Arial", Font.BOLD, 12));
        btnCerrar.setBackground(new Color(200, 200, 200));
        btnCerrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dialogTicket.dispose();
            }
        });
        
        JPanel panelBoton = new JPanel();
        panelBoton.setBackground(Color.WHITE);
        panelBoton.add(btnCerrar);
        
        dialogTicket.add(panelTicket, BorderLayout.CENTER);
        dialogTicket.add(panelBoton, BorderLayout.SOUTH);
        
        dialogTicket.setVisible(true);
    }

    private JLabel crearLabelNegrita(String texto) {
        JLabel label = new JLabel(texto);
        label.setFont(new Font("Arial", Font.BOLD, 12));
        label.setBackground(Color.WHITE);
        return label;
    }

    private JLabel crearLabel(String texto) {
        JLabel label = new JLabel(texto);
        label.setFont(new Font("Arial", Font.PLAIN, 12));
        label.setBackground(Color.WHITE);
        return label;
    }

    private void reservarAsiento(int fila, int columna) {
        if (asientos[fila][columna] == 'L') {
            // Guardar en el historial antes de reservar
            int[] reserva = {fila, columna};
            historialReservas.push(reserva);
            
            // Reservar asiento
            asientos[fila][columna] = 'X';
            botonesAsientos[fila][columna].setBackground(Color.RED);
            botonesAsientos[fila][columna].setText("X");
            agregarEstado("");
            agregarEstado("✓ RESERVA EXITOSA -  Fila: " + (fila + 1) + "  |  Asiento: " + (columna + 1));
            generarTicket(fila, columna);
        } else {
            // Asiento ya ocupado
            agregarEstado("");
            agregarEstado("✗ ERROR DE RESERVA");
            agregarEstado("  Fila: " + (fila + 1) + "  |  Asiento: " + (columna + 1));
            agregarEstado("  Motivo: Asiento ya esta OCUPADO (ROJO)");
            
            JOptionPane.showMessageDialog(this, 
                "ESTE ASIENTO YA ESTA OCUPADO (ROJO)\n\n" +
                "Por favor, seleccione un asiento VERDE (libre).",
                "RESERVA NO DISPONIBLE",
                JOptionPane.WARNING_MESSAGE);
        }
        
        // Verificar si ya no hay asientos libres
        if (contarAsientosLibres() == 0) {
            agregarEstado("");
            agregarEstado("ANFITEATRO COMPLETO");
            agregarEstado("No quedan asientos disponibles");
            JOptionPane.showMessageDialog(this, 
                "ANFITEATRO COMPLETO",
                "Capacidad Maxima Alcanzada",
                JOptionPane.INFORMATION_MESSAGE);
        }
    }
    
    private void deshacerReserva() {
        if (historialReservas.isEmpty()) {
            agregarEstado("");
            agregarEstado("⚠ NO HAY RESERVAS PARA DESHACER");
            JOptionPane.showMessageDialog(this, 
                "No hay reservas para deshacer.",
                "DESHACER NO DISPONIBLE",
                JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        
        // Obtener la última reserva
        int[] ultimaReserva = historialReservas.pop();
        int fila = ultimaReserva[0];
        int columna = ultimaReserva[1];
        
        // Liberar el asiento
        asientos[fila][columna] = 'L';
        botonesAsientos[fila][columna].setBackground(Color.GREEN);
        botonesAsientos[fila][columna].setText("F" + (fila + 1) + " A" + (columna + 1));
       
        JOptionPane.showMessageDialog(this, 
            "El asiento ahora esta disponible (VERDE).",
            "DESHACER RESERVA",
            JOptionPane.INFORMATION_MESSAGE);
    }
    
    private int contarAsientosLibres() {
        int libres = 0;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (asientos[i][j] == 'L') {
                    libres++;
                }
            }
        }
        return libres;
    }
    
    private void reiniciarSistema() {
        int confirm = JOptionPane.showConfirmDialog(this, 
            "¿REINICIAR SISTEMA COMPLETAMENTE?\n\n" +
            "Esta accion:\n" +
            "- Liberara todos los asientos (todos VERDES)\n" +
            "- Borrara todas las reservas actuales\n" +
            "- Eliminara el historial de reservas\n" +
            "¿Desea continuar?",
            "CONFIRMAR REINICIO",
            JOptionPane.YES_NO_OPTION,
            JOptionPane.WARNING_MESSAGE);
        
        if (confirm == JOptionPane.YES_OPTION) {
            // Reiniciar matriz de asientos
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    asientos[i][j] = 'L';
                    botonesAsientos[i][j].setBackground(Color.GREEN);
                    botonesAsientos[i][j].setText("F" + (i + 1) + " A" + (j + 1));
                }
            }
            
            // Limpiar historial
            historialReservas.clear();
            
            // Limpiar área de estado
            areaEstado.setText("");
            agregarEstado("=== SISTEMA REINICIADO COMPLETAMENTE ===");
            agregarEstado("Fecha/Hora: " + new java.util.Date().toString());
            agregarEstado("");
            agregarEstado("TODOS los asientos han sido LIBERADOS (VERDES)");
            agregarEstado("Las reservas anteriores han sido ELIMINADAS");
            agregarEstado("El historial de reservas ha sido VACIADO");
            agregarEstado("");
        } else {
            agregarEstado("Reinicio cancelado - Las reservas se mantienen");
        }
    }
    
    private void agregarEstado(String mensaje) {
        areaEstado.append(mensaje + "\n");
        areaEstado.setCaretPosition(areaEstado.getDocument().getLength());
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
                } catch (Exception e) {
                    e.printStackTrace();
                }
                new AnfiteatroGUI().setVisible(true);
            }
        });
    }
}