/****** Object:  Database [Geo]    Script Date: 06/07/2019 04:22:54 ******/
CREATE DATABASE [Geo]
GO
USE [Geo]
GO
CREATE TABLE [dbo].[Cidades](
	[IDCidade] [int] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](50) NULL,
	[IDEstado] [int] NOT NULL,
 CONSTRAINT [PK_Cidades] PRIMARY KEY CLUSTERED 
(
	[IDCidade] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Estados]    Script Date: 06/07/2019 04:22:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Estados](
	[IDEstado] [int] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](50) NULL,
	[Sigla] [varchar](10) NULL,
	[IDPais] [int] NOT NULL,
 CONSTRAINT [PK_Estados] PRIMARY KEY CLUSTERED 
(
	[IDEstado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[FileManagement]    Script Date: 06/07/2019 04:22:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FileManagement](
	[IDFile] [int] IDENTITY(1,1) NOT NULL,
	[NomeArquivo] [varchar](100) NOT NULL,
	[CreateFile] [datetime] NOT NULL,
 CONSTRAINT [PK_FileManagement] PRIMARY KEY CLUSTERED 
(
	[IDFile] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IdentificationPoint]    Script Date: 06/07/2019 04:22:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IdentificationPoint](
	[IDGeo] [int] IDENTITY(1,1) NOT NULL,
	[IDPoints] [int] NULL,
	[IDPais] [int] NULL,
	[IDEstado] [int] NULL,
	[IDCidades] [int] NULL,
	[IDLogradouro] [int] NULL,
 CONSTRAINT [PK_IdentificationPoint] PRIMARY KEY CLUSTERED 
(
	[IDGeo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Logradouros]    Script Date: 06/07/2019 04:22:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Logradouros](
	[IDLogradouro] [int] IDENTITY(1,1) NOT NULL,
	[Rua] [varchar](50) NULL,
	[Numero] [varchar](50) NULL,
	[bairro] [varchar](50) NULL,
	[CEP] [varchar](50) NULL,
	[IDCidade] [int] NOT NULL,
 CONSTRAINT [PK_Logradouros] PRIMARY KEY CLUSTERED 
(
	[IDLogradouro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Paises]    Script Date: 06/07/2019 04:22:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Paises](
	[IDPais] [int] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](50) NULL,
	[Sigla] [varchar](10) NULL,
 CONSTRAINT [PK_Pais] PRIMARY KEY CLUSTERED 
(
	[IDPais] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Points]    Script Date: 06/07/2019 04:22:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Points](
	[IDPoints] [int] IDENTITY(1,1) NOT NULL,
	[Latitude] [decimal](9, 6) NOT NULL,
	[Logintude] [decimal](9, 6) NOT NULL,
	[Distance] [varchar](20) NULL,
	[Bearing] [varchar](20) NULL,
	[IDFile] [int] NOT NULL,
 CONSTRAINT [PK_Points] PRIMARY KEY CLUSTERED 
(
	[IDPoints] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Cidades]  WITH CHECK ADD  CONSTRAINT [FK_Cidades_Estados1] FOREIGN KEY([IDEstado])
REFERENCES [dbo].[Estados] ([IDEstado])
GO
ALTER TABLE [dbo].[Cidades] CHECK CONSTRAINT [FK_Cidades_Estados1]
GO
ALTER TABLE [dbo].[Estados]  WITH CHECK ADD  CONSTRAINT [FK_Estados_Paises] FOREIGN KEY([IDPais])
REFERENCES [dbo].[Paises] ([IDPais])
GO
ALTER TABLE [dbo].[Estados] CHECK CONSTRAINT [FK_Estados_Paises]
GO
ALTER TABLE [dbo].[IdentificationPoint]  WITH CHECK ADD  CONSTRAINT [FK_IdentificationPoint_Cidades] FOREIGN KEY([IDCidades])
REFERENCES [dbo].[Cidades] ([IDCidade])
GO
ALTER TABLE [dbo].[IdentificationPoint] CHECK CONSTRAINT [FK_IdentificationPoint_Cidades]
GO
ALTER TABLE [dbo].[IdentificationPoint]  WITH CHECK ADD  CONSTRAINT [FK_IdentificationPoint_Estados] FOREIGN KEY([IDEstado])
REFERENCES [dbo].[Estados] ([IDEstado])
GO
ALTER TABLE [dbo].[IdentificationPoint] CHECK CONSTRAINT [FK_IdentificationPoint_Estados]
GO
ALTER TABLE [dbo].[IdentificationPoint]  WITH CHECK ADD  CONSTRAINT [FK_IdentificationPoint_Logradouros] FOREIGN KEY([IDLogradouro])
REFERENCES [dbo].[Logradouros] ([IDLogradouro])
GO
ALTER TABLE [dbo].[IdentificationPoint] CHECK CONSTRAINT [FK_IdentificationPoint_Logradouros]
GO
ALTER TABLE [dbo].[IdentificationPoint]  WITH CHECK ADD  CONSTRAINT [FK_IdentificationPoint_Paises] FOREIGN KEY([IDPais])
REFERENCES [dbo].[Paises] ([IDPais])
GO
ALTER TABLE [dbo].[IdentificationPoint] CHECK CONSTRAINT [FK_IdentificationPoint_Paises]
GO
ALTER TABLE [dbo].[IdentificationPoint]  WITH CHECK ADD  CONSTRAINT [FK_IdentificationPoint_Points] FOREIGN KEY([IDPoints])
REFERENCES [dbo].[Points] ([IDPoints])
GO
ALTER TABLE [dbo].[IdentificationPoint] CHECK CONSTRAINT [FK_IdentificationPoint_Points]
GO
ALTER TABLE [dbo].[Logradouros]  WITH CHECK ADD  CONSTRAINT [FK_Logradouros_Cidades1] FOREIGN KEY([IDCidade])
REFERENCES [dbo].[Cidades] ([IDCidade])
GO
ALTER TABLE [dbo].[Logradouros] CHECK CONSTRAINT [FK_Logradouros_Cidades1]
GO
ALTER TABLE [dbo].[Points]  WITH CHECK ADD  CONSTRAINT [FK_Points_FileManagement] FOREIGN KEY([IDFile])
REFERENCES [dbo].[FileManagement] ([IDFile])
GO
ALTER TABLE [dbo].[Points] CHECK CONSTRAINT [FK_Points_FileManagement]
GO
ALTER DATABASE [Geo] SET  READ_WRITE 
GO
