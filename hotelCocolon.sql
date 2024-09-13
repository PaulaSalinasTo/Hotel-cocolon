-- Crea la base de datos y usa la base de datos creada
DROP DATABASE IF EXISTS appHotelCocolon;
CREATE DATABASE appHotelCocolon;
USE appHotelCocolon;

-- Crea la tabla Clientes
CREATE TABLE Clientes (
    ci_cliente VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    direccion VARCHAR(255)
);

-- Crea la tabla Habitaciones
CREATE TABLE Habitaciones (
    id_habitacion INT AUTO_INCREMENT PRIMARY KEY,
    numero_habitacion INT UNIQUE NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'disponible'
);

-- Crea la tabla Reservas
CREATE TABLE Reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    ci_cliente VARCHAR(20),
    id_habitacion INT,
    fecha_entrada DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'reservado',
    FOREIGN KEY (ci_cliente) REFERENCES Clientes(ci_cliente),
    FOREIGN KEY (id_habitacion) REFERENCES Habitaciones(id_habitacion)
);

-- Crea la tabla Pagos
CREATE TABLE Pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_reserva INT,
    metodo_pago VARCHAR(50) NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    fecha_pago DATE NOT NULL,
    FOREIGN KEY (id_reserva) REFERENCES Reservas(id_reserva)
);

-- Inserta datos en la tabla Clientes
INSERT INTO Clientes (ci_cliente, nombre, apellido, email, telefono, direccion) VALUES
('1234567890', 'Juan', 'Pérez', 'juan.perez@example.com', '123456789', 'Av. Principal 123, Ciudad'),
('0987654321', 'Ana', 'Gómez', 'ana.gomez@example.com', '987654321', 'Calle Secundaria 456, Ciudad'),
('1122334455', 'Carlos', 'Lopez', 'carlos.lopez@example.com', '456789123', 'Av. Tercera 789, Ciudad'),
('5566778899', 'María', 'Martinez', 'maria.martinez@example.com', '321654987', 'Calle Cuarta 101, Ciudad'),
('6677889900', 'Laura', 'Sánchez', 'laura.sanchez@example.com', '654123789', 'Av. Quinta 202, Ciudad');

-- Inserta datos en la tabla Habitaciones
INSERT INTO Habitaciones (numero_habitacion, tipo, precio, estado) VALUES
(101, 'Simple', 50.00, 'disponible'),
(102, 'Doble', 75.00, 'disponible'),
(103, 'Suite', 120.00, 'ocupada'),
(104, 'Doble', 75.00, 'mantenimiento'),
(105, 'Simple', 50.00, 'disponible'),
(106, 'Suite', 120.00, 'disponible');

-- Consulta los id_habitacion generados
SELECT * FROM Habitaciones;

-- Inserta datos en la tabla Reservas usando los valores correctos de id_habitacion
INSERT INTO Reservas (ci_cliente, id_habitacion, fecha_entrada, fecha_salida, estado) VALUES
('1234567890', 1, '2024-09-15', '2024-09-18', 'reservado'),  -- id_habitacion 1 para numero_habitacion 101
('0987654321', 3, '2024-09-16', '2024-09-20', 'ocupada'),   -- id_habitacion 3 para numero_habitacion 103
('1122334455', 2, '2024-09-20', '2024-09-22', 'reservado'),  -- id_habitacion 2 para numero_habitacion 102
('5566778899', 5, '2024-09-18', '2024-09-19', 'cancelado'),  -- id_habitacion 5 para numero_habitacion 105
('6677889900', 6, '2024-09-25', '2024-09-28', 'reservado');  -- id_habitacion 6 para numero_habitacion 106

-- Inserta datos en la tabla Pagos
INSERT INTO Pagos (id_reserva, metodo_pago, monto, fecha_pago) VALUES
(1, 'Tarjeta de Crédito', 150.00, '2024-09-10'),
(2, 'Efectivo', 480.00, '2024-09-15'),
(3, 'Transferencia Bancaria', 150.00, '2024-09-18'),
(4, 'Tarjeta de Débito', 360.00, '2024-09-22');  -- Cambiado de 5 a 4 para que coincida con los ids de reserva existentes
