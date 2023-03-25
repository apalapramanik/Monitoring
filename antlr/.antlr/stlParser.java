// Generated from /home/apramani/STL RESEARCH/monitoring/antlr/stlParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class stlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MINUS=1, PLUS=2, TIMES=3, DIVIDE=4, LPAREN=5, RPAREN=6, LBRACE=7, RBRACE=8, 
		LBRACK=9, RBRACK=10, SEMICOLON=11, COLON=12, COMMA=13, DOT=14, AT=15, 
		ABS=16, SQRT=17, EXP=18, POW=19, SEC=20, MSEC=21, USEC=22, NSEC=23, ROS_Topic=24, 
		Import=25, Input=26, Output=27, Internal=28, Constant=29, DomainTypeReal=30, 
		DomainTypeFloat=31, DomainTypeLong=32, DomainTypeComplex=33, DomainTypeInt=34, 
		DomainTypeBool=35, Assertion=36, Specification=37, From=38, NotOperator=39, 
		OrOperator=40, AndOperator=41, IffOperator=42, ImpliesOperator=43, XorOperator=44, 
		RiseOperator=45, FallOperator=46, AlwaysOperator=47, EventuallyOperator=48, 
		UntilOperator=49, UnlessOperator=50, HistoricallyOperator=51, OnceOperator=52, 
		SinceOperator=53, NextOperator=54, PreviousOperator=55, EqualOperator=56, 
		NotEqualOperator=57, GreaterOrEqualOperator=58, LesserOrEqualOperator=59, 
		GreaterOperator=60, LesserOperator=61, EQUAL=62, BooleanLiteral=63, TRUE=64, 
		FALSE=65, IntegerLiteral=66, RealLiteral=67, Identifier=68, LINE_TERMINATOR=69, 
		WHITESPACE=70, COMMENT=71, LINE_COMMENT=72;
	public static final int
		RULE_specification_file = 0, RULE_specification = 1, RULE_spec = 2, RULE_modimport = 3, 
		RULE_assertion = 4, RULE_declaration = 5, RULE_annotation = 6, RULE_annotation_type = 7, 
		RULE_variableDeclaration = 8, RULE_constantDeclaration = 9, RULE_assignment = 10, 
		RULE_domainType = 11, RULE_ioType = 12, RULE_real_expression = 13, RULE_comparisonOp = 14, 
		RULE_literal = 15, RULE_identifier = 16, RULE_interval = 17, RULE_intervalTime = 18, 
		RULE_unit = 19, RULE_expression = 20;
	private static String[] makeRuleNames() {
		return new String[] {
			"specification_file", "specification", "spec", "modimport", "assertion", 
			"declaration", "annotation", "annotation_type", "variableDeclaration", 
			"constantDeclaration", "assignment", "domainType", "ioType", "real_expression", 
			"comparisonOp", "literal", "identifier", "interval", "intervalTime", 
			"unit", "expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'-'", "'+'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
			"']'", "';'", "':'", "','", "'.'", "'@'", "'abs'", "'sqrt'", "'exp'", 
			"'pow'", "'s'", "'ms'", "'us'", "'ns'", "'topic'", "'import'", "'input'", 
			"'output'", "'internal'", "'const'", "'real'", "'float'", "'long'", "'complex'", 
			"'int'", "'bool'", "'assertion'", "'specification'", "'from'", null, 
			null, null, null, null, "'xor'", "'rise'", "'fall'", null, null, null, 
			null, null, null, null, null, null, "'=='", "'!=='", "'>='", "'<='", 
			"'>'", "'<'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MINUS", "PLUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "LBRACK", "RBRACK", "SEMICOLON", "COLON", "COMMA", "DOT", "AT", 
			"ABS", "SQRT", "EXP", "POW", "SEC", "MSEC", "USEC", "NSEC", "ROS_Topic", 
			"Import", "Input", "Output", "Internal", "Constant", "DomainTypeReal", 
			"DomainTypeFloat", "DomainTypeLong", "DomainTypeComplex", "DomainTypeInt", 
			"DomainTypeBool", "Assertion", "Specification", "From", "NotOperator", 
			"OrOperator", "AndOperator", "IffOperator", "ImpliesOperator", "XorOperator", 
			"RiseOperator", "FallOperator", "AlwaysOperator", "EventuallyOperator", 
			"UntilOperator", "UnlessOperator", "HistoricallyOperator", "OnceOperator", 
			"SinceOperator", "NextOperator", "PreviousOperator", "EqualOperator", 
			"NotEqualOperator", "GreaterOrEqualOperator", "LesserOrEqualOperator", 
			"GreaterOperator", "LesserOperator", "EQUAL", "BooleanLiteral", "TRUE", 
			"FALSE", "IntegerLiteral", "RealLiteral", "Identifier", "LINE_TERMINATOR", 
			"WHITESPACE", "COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "stlParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public stlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Specification_fileContext extends ParserRuleContext {
		public SpecificationContext specification() {
			return getRuleContext(SpecificationContext.class,0);
		}
		public TerminalNode EOF() { return getToken(stlParser.EOF, 0); }
		public Specification_fileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specification_file; }
	}

	public final Specification_fileContext specification_file() throws RecognitionException {
		Specification_fileContext _localctx = new Specification_fileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_specification_file);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			specification();
			setState(43);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SpecificationContext extends ParserRuleContext {
		public SpecContext spec() {
			return getRuleContext(SpecContext.class,0);
		}
		public List<ModimportContext> modimport() {
			return getRuleContexts(ModimportContext.class);
		}
		public ModimportContext modimport(int i) {
			return getRuleContext(ModimportContext.class,i);
		}
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<AnnotationContext> annotation() {
			return getRuleContexts(AnnotationContext.class);
		}
		public AnnotationContext annotation(int i) {
			return getRuleContext(AnnotationContext.class,i);
		}
		public List<AssertionContext> assertion() {
			return getRuleContexts(AssertionContext.class);
		}
		public AssertionContext assertion(int i) {
			return getRuleContext(AssertionContext.class,i);
		}
		public SpecificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specification; }
	}

	public final SpecificationContext specification() throws RecognitionException {
		SpecificationContext _localctx = new SpecificationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_specification);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Specification) {
				{
				setState(45);
				spec();
				}
			}

			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==From) {
				{
				{
				setState(48);
				modimport();
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(58);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(56);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case Input:
					case Output:
					case Constant:
					case DomainTypeFloat:
					case DomainTypeLong:
					case DomainTypeComplex:
					case DomainTypeInt:
					case Identifier:
						{
						setState(54);
						declaration();
						}
						break;
					case AT:
						{
						setState(55);
						annotation();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(60);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(62); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(61);
				assertion();
				}
				}
				setState(64); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MINUS) | (1L << LPAREN) | (1L << ABS) | (1L << SQRT) | (1L << EXP) | (1L << POW) | (1L << NotOperator) | (1L << RiseOperator) | (1L << FallOperator) | (1L << AlwaysOperator) | (1L << EventuallyOperator) | (1L << HistoricallyOperator) | (1L << OnceOperator) | (1L << NextOperator) | (1L << PreviousOperator))) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & ((1L << (IntegerLiteral - 66)) | (1L << (RealLiteral - 66)) | (1L << (Identifier - 66)))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SpecContext extends ParserRuleContext {
		public SpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_spec; }
	 
		public SpecContext() { }
		public void copyFrom(SpecContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SpecificationIdContext extends SpecContext {
		public TerminalNode Specification() { return getToken(stlParser.Specification, 0); }
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public SpecificationIdContext(SpecContext ctx) { copyFrom(ctx); }
	}

	public final SpecContext spec() throws RecognitionException {
		SpecContext _localctx = new SpecContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_spec);
		try {
			_localctx = new SpecificationIdContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(Specification);
			setState(67);
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ModimportContext extends ParserRuleContext {
		public ModimportContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modimport; }
	 
		public ModimportContext() { }
		public void copyFrom(ModimportContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ModImportContext extends ModimportContext {
		public TerminalNode From() { return getToken(stlParser.From, 0); }
		public List<TerminalNode> Identifier() { return getTokens(stlParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(stlParser.Identifier, i);
		}
		public TerminalNode Import() { return getToken(stlParser.Import, 0); }
		public ModImportContext(ModimportContext ctx) { copyFrom(ctx); }
	}

	public final ModimportContext modimport() throws RecognitionException {
		ModimportContext _localctx = new ModimportContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_modimport);
		try {
			_localctx = new ModImportContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(From);
			setState(70);
			match(Identifier);
			setState(71);
			match(Import);
			setState(72);
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssertionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public TerminalNode EQUAL() { return getToken(stlParser.EQUAL, 0); }
		public AssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion; }
	}

	public final AssertionContext assertion() throws RecognitionException {
		AssertionContext _localctx = new AssertionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assertion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(74);
				match(Identifier);
				setState(75);
				match(EQUAL);
				}
				break;
			}
			setState(78);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	 
		public DeclarationContext() { }
		public void copyFrom(DeclarationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class DeclVariableContext extends DeclarationContext {
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public DeclVariableContext(DeclarationContext ctx) { copyFrom(ctx); }
	}
	public static class DeclConstantContext extends DeclarationContext {
		public ConstantDeclarationContext constantDeclaration() {
			return getRuleContext(ConstantDeclarationContext.class,0);
		}
		public DeclConstantContext(DeclarationContext ctx) { copyFrom(ctx); }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declaration);
		try {
			setState(82);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Input:
			case Output:
			case DomainTypeFloat:
			case DomainTypeLong:
			case DomainTypeComplex:
			case DomainTypeInt:
			case Identifier:
				_localctx = new DeclVariableContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				variableDeclaration();
				}
				break;
			case Constant:
				_localctx = new DeclConstantContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(81);
				constantDeclaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AnnotationContext extends ParserRuleContext {
		public TerminalNode AT() { return getToken(stlParser.AT, 0); }
		public Annotation_typeContext annotation_type() {
			return getRuleContext(Annotation_typeContext.class,0);
		}
		public AnnotationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_annotation; }
	}

	public final AnnotationContext annotation() throws RecognitionException {
		AnnotationContext _localctx = new AnnotationContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_annotation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(AT);
			setState(85);
			annotation_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Annotation_typeContext extends ParserRuleContext {
		public Annotation_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_annotation_type; }
	 
		public Annotation_typeContext() { }
		public void copyFrom(Annotation_typeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class RosTopicContext extends Annotation_typeContext {
		public TerminalNode ROS_Topic() { return getToken(stlParser.ROS_Topic, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public List<TerminalNode> Identifier() { return getTokens(stlParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(stlParser.Identifier, i);
		}
		public TerminalNode COMMA() { return getToken(stlParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public RosTopicContext(Annotation_typeContext ctx) { copyFrom(ctx); }
	}

	public final Annotation_typeContext annotation_type() throws RecognitionException {
		Annotation_typeContext _localctx = new Annotation_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_annotation_type);
		try {
			_localctx = new RosTopicContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(ROS_Topic);
			setState(88);
			match(LPAREN);
			setState(89);
			match(Identifier);
			setState(90);
			match(COMMA);
			setState(91);
			match(Identifier);
			setState(92);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclarationContext extends ParserRuleContext {
		public DomainTypeContext domainType() {
			return getRuleContext(DomainTypeContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public IoTypeContext ioType() {
			return getRuleContext(IoTypeContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_variableDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Input || _la==Output) {
				{
				setState(94);
				ioType();
				}
			}

			setState(97);
			domainType();
			setState(98);
			match(Identifier);
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(99);
				assignment();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstantDeclarationContext extends ParserRuleContext {
		public TerminalNode Constant() { return getToken(stlParser.Constant, 0); }
		public DomainTypeContext domainType() {
			return getRuleContext(DomainTypeContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public TerminalNode EQUAL() { return getToken(stlParser.EQUAL, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ConstantDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantDeclaration; }
	}

	public final ConstantDeclarationContext constantDeclaration() throws RecognitionException {
		ConstantDeclarationContext _localctx = new ConstantDeclarationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constantDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(Constant);
			setState(103);
			domainType();
			setState(104);
			match(Identifier);
			setState(105);
			match(EQUAL);
			setState(106);
			literal();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	 
		public AssignmentContext() { }
		public void copyFrom(AssignmentContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AsgnExprContext extends AssignmentContext {
		public TerminalNode EQUAL() { return getToken(stlParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AsgnExprContext(AssignmentContext ctx) { copyFrom(ctx); }
	}
	public static class AsgnLiteralContext extends AssignmentContext {
		public TerminalNode EQUAL() { return getToken(stlParser.EQUAL, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public AsgnLiteralContext(AssignmentContext ctx) { copyFrom(ctx); }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assignment);
		try {
			setState(112);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				_localctx = new AsgnLiteralContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				match(EQUAL);
				setState(109);
				literal();
				}
				break;
			case 2:
				_localctx = new AsgnExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				match(EQUAL);
				setState(111);
				expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DomainTypeContext extends ParserRuleContext {
		public TerminalNode DomainTypeFloat() { return getToken(stlParser.DomainTypeFloat, 0); }
		public TerminalNode DomainTypeInt() { return getToken(stlParser.DomainTypeInt, 0); }
		public TerminalNode DomainTypeLong() { return getToken(stlParser.DomainTypeLong, 0); }
		public TerminalNode DomainTypeComplex() { return getToken(stlParser.DomainTypeComplex, 0); }
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public DomainTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_domainType; }
	}

	public final DomainTypeContext domainType() throws RecognitionException {
		DomainTypeContext _localctx = new DomainTypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_domainType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			_la = _input.LA(1);
			if ( !(((((_la - 31)) & ~0x3f) == 0 && ((1L << (_la - 31)) & ((1L << (DomainTypeFloat - 31)) | (1L << (DomainTypeLong - 31)) | (1L << (DomainTypeComplex - 31)) | (1L << (DomainTypeInt - 31)) | (1L << (Identifier - 31)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IoTypeContext extends ParserRuleContext {
		public TerminalNode Input() { return getToken(stlParser.Input, 0); }
		public TerminalNode Output() { return getToken(stlParser.Output, 0); }
		public IoTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ioType; }
	}

	public final IoTypeContext ioType() throws RecognitionException {
		IoTypeContext _localctx = new IoTypeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_ioType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			_la = _input.LA(1);
			if ( !(_la==Input || _la==Output) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Real_expressionContext extends ParserRuleContext {
		public Real_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_real_expression; }
	 
		public Real_expressionContext() { }
		public void copyFrom(Real_expressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExprSubtractionContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(stlParser.MINUS, 0); }
		public ExprSubtractionContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprPowContext extends Real_expressionContext {
		public TerminalNode POW() { return getToken(stlParser.POW, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(stlParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprPowContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprDivisionContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode DIVIDE() { return getToken(stlParser.DIVIDE, 0); }
		public ExprDivisionContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprMultiplicationContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode TIMES() { return getToken(stlParser.TIMES, 0); }
		public ExprMultiplicationContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprLiteralContext extends Real_expressionContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ExprLiteralContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprExpContext extends Real_expressionContext {
		public TerminalNode EXP() { return getToken(stlParser.EXP, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprExpContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprSqrtContext extends Real_expressionContext {
		public TerminalNode SQRT() { return getToken(stlParser.SQRT, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprSqrtContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprIdContext extends Real_expressionContext {
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public ExprIdContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAbsContext extends Real_expressionContext {
		public TerminalNode ABS() { return getToken(stlParser.ABS, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprAbsContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAdditionContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(stlParser.PLUS, 0); }
		public ExprAdditionContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}

	public final Real_expressionContext real_expression() throws RecognitionException {
		return real_expression(0);
	}

	private Real_expressionContext real_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Real_expressionContext _localctx = new Real_expressionContext(_ctx, _parentState);
		Real_expressionContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_real_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Identifier:
				{
				_localctx = new ExprIdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(119);
				match(Identifier);
				}
				break;
			case MINUS:
			case IntegerLiteral:
			case RealLiteral:
				{
				_localctx = new ExprLiteralContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(120);
				literal();
				}
				break;
			case ABS:
				{
				_localctx = new ExprAbsContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(121);
				match(ABS);
				setState(122);
				match(LPAREN);
				setState(123);
				real_expression(0);
				setState(124);
				match(RPAREN);
				}
				break;
			case SQRT:
				{
				_localctx = new ExprSqrtContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(126);
				match(SQRT);
				setState(127);
				match(LPAREN);
				setState(128);
				real_expression(0);
				setState(129);
				match(RPAREN);
				}
				break;
			case EXP:
				{
				_localctx = new ExprExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(131);
				match(EXP);
				setState(132);
				match(LPAREN);
				setState(133);
				real_expression(0);
				setState(134);
				match(RPAREN);
				}
				break;
			case POW:
				{
				_localctx = new ExprPowContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(136);
				match(POW);
				setState(137);
				match(LPAREN);
				setState(138);
				real_expression(0);
				setState(139);
				match(COMMA);
				setState(140);
				real_expression(0);
				setState(141);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(159);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(157);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new ExprAdditionContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(145);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(146);
						match(PLUS);
						setState(147);
						real_expression(9);
						}
						break;
					case 2:
						{
						_localctx = new ExprSubtractionContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(148);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(149);
						match(MINUS);
						setState(150);
						real_expression(8);
						}
						break;
					case 3:
						{
						_localctx = new ExprMultiplicationContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(151);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(152);
						match(TIMES);
						setState(153);
						real_expression(7);
						}
						break;
					case 4:
						{
						_localctx = new ExprDivisionContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(154);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(155);
						match(DIVIDE);
						setState(156);
						real_expression(6);
						}
						break;
					}
					} 
				}
				setState(161);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ComparisonOpContext extends ParserRuleContext {
		public ComparisonOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonOp; }
	 
		public ComparisonOpContext() { }
		public void copyFrom(ComparisonOpContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class GeqContext extends ComparisonOpContext {
		public TerminalNode GreaterOrEqualOperator() { return getToken(stlParser.GreaterOrEqualOperator, 0); }
		public GeqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class LeqContext extends ComparisonOpContext {
		public TerminalNode LesserOrEqualOperator() { return getToken(stlParser.LesserOrEqualOperator, 0); }
		public LeqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterContext extends ComparisonOpContext {
		public TerminalNode GreaterOperator() { return getToken(stlParser.GreaterOperator, 0); }
		public GreaterContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class NeqContext extends ComparisonOpContext {
		public TerminalNode NotEqualOperator() { return getToken(stlParser.NotEqualOperator, 0); }
		public NeqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class EqContext extends ComparisonOpContext {
		public TerminalNode EqualOperator() { return getToken(stlParser.EqualOperator, 0); }
		public EqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class LessContext extends ComparisonOpContext {
		public TerminalNode LesserOperator() { return getToken(stlParser.LesserOperator, 0); }
		public LessContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}

	public final ComparisonOpContext comparisonOp() throws RecognitionException {
		ComparisonOpContext _localctx = new ComparisonOpContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_comparisonOp);
		try {
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LesserOrEqualOperator:
				_localctx = new LeqContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				match(LesserOrEqualOperator);
				}
				break;
			case GreaterOrEqualOperator:
				_localctx = new GeqContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				match(GreaterOrEqualOperator);
				}
				break;
			case LesserOperator:
				_localctx = new LessContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(164);
				match(LesserOperator);
				}
				break;
			case GreaterOperator:
				_localctx = new GreaterContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(165);
				match(GreaterOperator);
				}
				break;
			case EqualOperator:
				_localctx = new EqContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(166);
				match(EqualOperator);
				}
				break;
			case NotEqualOperator:
				_localctx = new NeqContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(167);
				match(NotEqualOperator);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode IntegerLiteral() { return getToken(stlParser.IntegerLiteral, 0); }
		public TerminalNode RealLiteral() { return getToken(stlParser.RealLiteral, 0); }
		public TerminalNode MINUS() { return getToken(stlParser.MINUS, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_literal);
		try {
			setState(174);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IntegerLiteral:
				enterOuterAlt(_localctx, 1);
				{
				setState(170);
				match(IntegerLiteral);
				}
				break;
			case RealLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(171);
				match(RealLiteral);
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(172);
				match(MINUS);
				setState(173);
				literal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	 
		public IdentifierContext() { }
		public void copyFrom(IdentifierContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IdContext extends IdentifierContext {
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public IdContext(IdentifierContext ctx) { copyFrom(ctx); }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_identifier);
		try {
			_localctx = new IdContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntervalContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(stlParser.LBRACK, 0); }
		public List<IntervalTimeContext> intervalTime() {
			return getRuleContexts(IntervalTimeContext.class);
		}
		public IntervalTimeContext intervalTime(int i) {
			return getRuleContext(IntervalTimeContext.class,i);
		}
		public TerminalNode RBRACK() { return getToken(stlParser.RBRACK, 0); }
		public TerminalNode COLON() { return getToken(stlParser.COLON, 0); }
		public TerminalNode COMMA() { return getToken(stlParser.COMMA, 0); }
		public IntervalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interval; }
	}

	public final IntervalContext interval() throws RecognitionException {
		IntervalContext _localctx = new IntervalContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_interval);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(LBRACK);
			setState(179);
			intervalTime();
			setState(180);
			_la = _input.LA(1);
			if ( !(_la==COLON || _la==COMMA) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(181);
			intervalTime();
			setState(182);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntervalTimeContext extends ParserRuleContext {
		public IntervalTimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intervalTime; }
	 
		public IntervalTimeContext() { }
		public void copyFrom(IntervalTimeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IntervalTimeLiteralContext extends IntervalTimeContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public IntervalTimeLiteralContext(IntervalTimeContext ctx) { copyFrom(ctx); }
	}
	public static class ConstantTimeLiteralContext extends IntervalTimeContext {
		public TerminalNode Identifier() { return getToken(stlParser.Identifier, 0); }
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public ConstantTimeLiteralContext(IntervalTimeContext ctx) { copyFrom(ctx); }
	}

	public final IntervalTimeContext intervalTime() throws RecognitionException {
		IntervalTimeContext _localctx = new IntervalTimeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_intervalTime);
		int _la;
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
			case IntegerLiteral:
			case RealLiteral:
				_localctx = new IntervalTimeLiteralContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
				literal();
				setState(186);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEC) | (1L << MSEC) | (1L << USEC) | (1L << NSEC))) != 0)) {
					{
					setState(185);
					unit();
					}
				}

				}
				break;
			case Identifier:
				_localctx = new ConstantTimeLiteralContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(188);
				match(Identifier);
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEC) | (1L << MSEC) | (1L << USEC) | (1L << NSEC))) != 0)) {
					{
					setState(189);
					unit();
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnitContext extends ParserRuleContext {
		public TerminalNode SEC() { return getToken(stlParser.SEC, 0); }
		public TerminalNode MSEC() { return getToken(stlParser.MSEC, 0); }
		public TerminalNode USEC() { return getToken(stlParser.USEC, 0); }
		public TerminalNode NSEC() { return getToken(stlParser.NSEC, 0); }
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_unit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEC) | (1L << MSEC) | (1L << USEC) | (1L << NSEC))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExprSinceContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode SinceOperator() { return getToken(stlParser.SinceOperator, 0); }
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExprSinceContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprParenContext extends ExpressionContext {
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprParenContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprIffContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode IffOperator() { return getToken(stlParser.IffOperator, 0); }
		public ExprIffContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExpreOnceContext extends ExpressionContext {
		public TerminalNode OnceOperator() { return getToken(stlParser.OnceOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExpreOnceContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprEvContext extends ExpressionContext {
		public TerminalNode EventuallyOperator() { return getToken(stlParser.EventuallyOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExprEvContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprImpliesContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ImpliesOperator() { return getToken(stlParser.ImpliesOperator, 0); }
		public ExprImpliesContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprUntilContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode UntilOperator() { return getToken(stlParser.UntilOperator, 0); }
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExprUntilContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprNotContext extends ExpressionContext {
		public TerminalNode NotOperator() { return getToken(stlParser.NotOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprNotContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprNextContext extends ExpressionContext {
		public TerminalNode NextOperator() { return getToken(stlParser.NextOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprNextContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAndContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AndOperator() { return getToken(stlParser.AndOperator, 0); }
		public ExprAndContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprUnlessContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode UnlessOperator() { return getToken(stlParser.UnlessOperator, 0); }
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExprUnlessContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprPreviousContext extends ExpressionContext {
		public TerminalNode PreviousOperator() { return getToken(stlParser.PreviousOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprPreviousContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprHistContext extends ExpressionContext {
		public TerminalNode HistoricallyOperator() { return getToken(stlParser.HistoricallyOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExprHistContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprFallContext extends ExpressionContext {
		public TerminalNode FallOperator() { return getToken(stlParser.FallOperator, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprFallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprPredicateContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ComparisonOpContext comparisonOp() {
			return getRuleContext(ComparisonOpContext.class,0);
		}
		public ExprPredicateContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprXorContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode XorOperator() { return getToken(stlParser.XorOperator, 0); }
		public ExprXorContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprRiseContext extends ExpressionContext {
		public TerminalNode RiseOperator() { return getToken(stlParser.RiseOperator, 0); }
		public TerminalNode LPAREN() { return getToken(stlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(stlParser.RPAREN, 0); }
		public ExprRiseContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprOrContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OrOperator() { return getToken(stlParser.OrOperator, 0); }
		public ExprOrContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAlwaysContext extends ExpressionContext {
		public TerminalNode AlwaysOperator() { return getToken(stlParser.AlwaysOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IntervalContext interval() {
			return getRuleContext(IntervalContext.class,0);
		}
		public ExprAlwaysContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprRealContext extends ExpressionContext {
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public ExprRealContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
			case ABS:
			case SQRT:
			case EXP:
			case POW:
			case IntegerLiteral:
			case RealLiteral:
			case Identifier:
				{
				_localctx = new ExprRealContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(197);
				real_expression(0);
				}
				break;
			case LPAREN:
				{
				_localctx = new ExprParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(198);
				match(LPAREN);
				setState(199);
				expression(0);
				setState(200);
				match(RPAREN);
				}
				break;
			case NotOperator:
				{
				_localctx = new ExprNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(202);
				match(NotOperator);
				setState(203);
				expression(17);
				}
				break;
			case AlwaysOperator:
				{
				_localctx = new ExprAlwaysContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(204);
				match(AlwaysOperator);
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBRACK) {
					{
					setState(205);
					interval();
					}
				}

				setState(208);
				expression(11);
				}
				break;
			case EventuallyOperator:
				{
				_localctx = new ExprEvContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(209);
				match(EventuallyOperator);
				setState(211);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBRACK) {
					{
					setState(210);
					interval();
					}
				}

				setState(213);
				expression(10);
				}
				break;
			case HistoricallyOperator:
				{
				_localctx = new ExprHistContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(214);
				match(HistoricallyOperator);
				setState(216);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBRACK) {
					{
					setState(215);
					interval();
					}
				}

				setState(218);
				expression(7);
				}
				break;
			case OnceOperator:
				{
				_localctx = new ExpreOnceContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(219);
				match(OnceOperator);
				setState(221);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LBRACK) {
					{
					setState(220);
					interval();
					}
				}

				setState(223);
				expression(6);
				}
				break;
			case RiseOperator:
				{
				_localctx = new ExprRiseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(224);
				match(RiseOperator);
				setState(225);
				match(LPAREN);
				setState(226);
				expression(0);
				setState(227);
				match(RPAREN);
				}
				break;
			case FallOperator:
				{
				_localctx = new ExprFallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(229);
				match(FallOperator);
				setState(230);
				match(LPAREN);
				setState(231);
				expression(0);
				setState(232);
				match(RPAREN);
				}
				break;
			case PreviousOperator:
				{
				_localctx = new ExprPreviousContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(234);
				match(PreviousOperator);
				setState(235);
				expression(2);
				}
				break;
			case NextOperator:
				{
				_localctx = new ExprNextContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(236);
				match(NextOperator);
				setState(237);
				expression(1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(279);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(277);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
					case 1:
						{
						_localctx = new ExprPredicateContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(240);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(241);
						comparisonOp();
						setState(242);
						expression(20);
						}
						break;
					case 2:
						{
						_localctx = new ExprOrContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(244);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(245);
						match(OrOperator);
						setState(246);
						expression(17);
						}
						break;
					case 3:
						{
						_localctx = new ExprAndContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(247);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(248);
						match(AndOperator);
						setState(249);
						expression(16);
						}
						break;
					case 4:
						{
						_localctx = new ExprImpliesContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(250);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(251);
						match(ImpliesOperator);
						setState(252);
						expression(15);
						}
						break;
					case 5:
						{
						_localctx = new ExprIffContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(253);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(254);
						match(IffOperator);
						setState(255);
						expression(14);
						}
						break;
					case 6:
						{
						_localctx = new ExprXorContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(256);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(257);
						match(XorOperator);
						setState(258);
						expression(13);
						}
						break;
					case 7:
						{
						_localctx = new ExprUntilContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(259);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(260);
						match(UntilOperator);
						setState(262);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==LBRACK) {
							{
							setState(261);
							interval();
							}
						}

						setState(264);
						expression(10);
						}
						break;
					case 8:
						{
						_localctx = new ExprUnlessContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(265);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(266);
						match(UnlessOperator);
						setState(268);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==LBRACK) {
							{
							setState(267);
							interval();
							}
						}

						setState(270);
						expression(9);
						}
						break;
					case 9:
						{
						_localctx = new ExprSinceContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(271);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(272);
						match(SinceOperator);
						setState(274);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==LBRACK) {
							{
							setState(273);
							interval();
							}
						}

						setState(276);
						expression(6);
						}
						break;
					}
					} 
				}
				setState(281);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return real_expression_sempred((Real_expressionContext)_localctx, predIndex);
		case 20:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean real_expression_sempred(Real_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 8);
		case 1:
			return precpred(_ctx, 7);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 19);
		case 5:
			return precpred(_ctx, 16);
		case 6:
			return precpred(_ctx, 15);
		case 7:
			return precpred(_ctx, 14);
		case 8:
			return precpred(_ctx, 13);
		case 9:
			return precpred(_ctx, 12);
		case 10:
			return precpred(_ctx, 9);
		case 11:
			return precpred(_ctx, 8);
		case 12:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3J\u011d\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\3\5\3\61\n\3\3"+
		"\3\7\3\64\n\3\f\3\16\3\67\13\3\3\3\3\3\7\3;\n\3\f\3\16\3>\13\3\3\3\6\3"+
		"A\n\3\r\3\16\3B\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6O\n\6\3\6\3"+
		"\6\3\7\3\7\5\7U\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\5\nb\n"+
		"\n\3\n\3\n\3\n\5\ng\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f"+
		"\5\fs\n\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\5\17\u0092\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\7\17\u00a0\n\17\f\17\16\17\u00a3\13\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\5\20\u00ab\n\20\3\21\3\21\3\21\3\21\5\21\u00b1\n"+
		"\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u00bd\n\24"+
		"\3\24\3\24\5\24\u00c1\n\24\5\24\u00c3\n\24\3\25\3\25\3\26\3\26\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00d1\n\26\3\26\3\26\3\26\5\26"+
		"\u00d6\n\26\3\26\3\26\3\26\5\26\u00db\n\26\3\26\3\26\3\26\5\26\u00e0\n"+
		"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3"+
		"\26\3\26\5\26\u00f1\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26"+
		"\u0109\n\26\3\26\3\26\3\26\3\26\5\26\u010f\n\26\3\26\3\26\3\26\3\26\5"+
		"\26\u0115\n\26\3\26\7\26\u0118\n\26\f\26\16\26\u011b\13\26\3\26\2\4\34"+
		"*\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*\2\6\4\2!$FF\3\2\34"+
		"\35\3\2\16\17\3\2\26\31\2\u013e\2,\3\2\2\2\4\60\3\2\2\2\6D\3\2\2\2\bG"+
		"\3\2\2\2\nN\3\2\2\2\fT\3\2\2\2\16V\3\2\2\2\20Y\3\2\2\2\22a\3\2\2\2\24"+
		"h\3\2\2\2\26r\3\2\2\2\30t\3\2\2\2\32v\3\2\2\2\34\u0091\3\2\2\2\36\u00aa"+
		"\3\2\2\2 \u00b0\3\2\2\2\"\u00b2\3\2\2\2$\u00b4\3\2\2\2&\u00c2\3\2\2\2"+
		"(\u00c4\3\2\2\2*\u00f0\3\2\2\2,-\5\4\3\2-.\7\2\2\3.\3\3\2\2\2/\61\5\6"+
		"\4\2\60/\3\2\2\2\60\61\3\2\2\2\61\65\3\2\2\2\62\64\5\b\5\2\63\62\3\2\2"+
		"\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66<\3\2\2\2\67\65\3\2\2\2"+
		"8;\5\f\7\29;\5\16\b\2:8\3\2\2\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2"+
		"\2=@\3\2\2\2><\3\2\2\2?A\5\n\6\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2"+
		"\2C\5\3\2\2\2DE\7\'\2\2EF\7F\2\2F\7\3\2\2\2GH\7(\2\2HI\7F\2\2IJ\7\33\2"+
		"\2JK\7F\2\2K\t\3\2\2\2LM\7F\2\2MO\7@\2\2NL\3\2\2\2NO\3\2\2\2OP\3\2\2\2"+
		"PQ\5*\26\2Q\13\3\2\2\2RU\5\22\n\2SU\5\24\13\2TR\3\2\2\2TS\3\2\2\2U\r\3"+
		"\2\2\2VW\7\21\2\2WX\5\20\t\2X\17\3\2\2\2YZ\7\32\2\2Z[\7\7\2\2[\\\7F\2"+
		"\2\\]\7\17\2\2]^\7F\2\2^_\7\b\2\2_\21\3\2\2\2`b\5\32\16\2a`\3\2\2\2ab"+
		"\3\2\2\2bc\3\2\2\2cd\5\30\r\2df\7F\2\2eg\5\26\f\2fe\3\2\2\2fg\3\2\2\2"+
		"g\23\3\2\2\2hi\7\37\2\2ij\5\30\r\2jk\7F\2\2kl\7@\2\2lm\5 \21\2m\25\3\2"+
		"\2\2no\7@\2\2os\5 \21\2pq\7@\2\2qs\5*\26\2rn\3\2\2\2rp\3\2\2\2s\27\3\2"+
		"\2\2tu\t\2\2\2u\31\3\2\2\2vw\t\3\2\2w\33\3\2\2\2xy\b\17\1\2y\u0092\7F"+
		"\2\2z\u0092\5 \21\2{|\7\22\2\2|}\7\7\2\2}~\5\34\17\2~\177\7\b\2\2\177"+
		"\u0092\3\2\2\2\u0080\u0081\7\23\2\2\u0081\u0082\7\7\2\2\u0082\u0083\5"+
		"\34\17\2\u0083\u0084\7\b\2\2\u0084\u0092\3\2\2\2\u0085\u0086\7\24\2\2"+
		"\u0086\u0087\7\7\2\2\u0087\u0088\5\34\17\2\u0088\u0089\7\b\2\2\u0089\u0092"+
		"\3\2\2\2\u008a\u008b\7\25\2\2\u008b\u008c\7\7\2\2\u008c\u008d\5\34\17"+
		"\2\u008d\u008e\7\17\2\2\u008e\u008f\5\34\17\2\u008f\u0090\7\b\2\2\u0090"+
		"\u0092\3\2\2\2\u0091x\3\2\2\2\u0091z\3\2\2\2\u0091{\3\2\2\2\u0091\u0080"+
		"\3\2\2\2\u0091\u0085\3\2\2\2\u0091\u008a\3\2\2\2\u0092\u00a1\3\2\2\2\u0093"+
		"\u0094\f\n\2\2\u0094\u0095\7\4\2\2\u0095\u00a0\5\34\17\13\u0096\u0097"+
		"\f\t\2\2\u0097\u0098\7\3\2\2\u0098\u00a0\5\34\17\n\u0099\u009a\f\b\2\2"+
		"\u009a\u009b\7\5\2\2\u009b\u00a0\5\34\17\t\u009c\u009d\f\7\2\2\u009d\u009e"+
		"\7\6\2\2\u009e\u00a0\5\34\17\b\u009f\u0093\3\2\2\2\u009f\u0096\3\2\2\2"+
		"\u009f\u0099\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f"+
		"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\35\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4"+
		"\u00ab\7=\2\2\u00a5\u00ab\7<\2\2\u00a6\u00ab\7?\2\2\u00a7\u00ab\7>\2\2"+
		"\u00a8\u00ab\7:\2\2\u00a9\u00ab\7;\2\2\u00aa\u00a4\3\2\2\2\u00aa\u00a5"+
		"\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa"+
		"\u00a9\3\2\2\2\u00ab\37\3\2\2\2\u00ac\u00b1\7D\2\2\u00ad\u00b1\7E\2\2"+
		"\u00ae\u00af\7\3\2\2\u00af\u00b1\5 \21\2\u00b0\u00ac\3\2\2\2\u00b0\u00ad"+
		"\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1!\3\2\2\2\u00b2\u00b3\7F\2\2\u00b3#"+
		"\3\2\2\2\u00b4\u00b5\7\13\2\2\u00b5\u00b6\5&\24\2\u00b6\u00b7\t\4\2\2"+
		"\u00b7\u00b8\5&\24\2\u00b8\u00b9\7\f\2\2\u00b9%\3\2\2\2\u00ba\u00bc\5"+
		" \21\2\u00bb\u00bd\5(\25\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd"+
		"\u00c3\3\2\2\2\u00be\u00c0\7F\2\2\u00bf\u00c1\5(\25\2\u00c0\u00bf\3\2"+
		"\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c2"+
		"\u00be\3\2\2\2\u00c3\'\3\2\2\2\u00c4\u00c5\t\5\2\2\u00c5)\3\2\2\2\u00c6"+
		"\u00c7\b\26\1\2\u00c7\u00f1\5\34\17\2\u00c8\u00c9\7\7\2\2\u00c9\u00ca"+
		"\5*\26\2\u00ca\u00cb\7\b\2\2\u00cb\u00f1\3\2\2\2\u00cc\u00cd\7)\2\2\u00cd"+
		"\u00f1\5*\26\23\u00ce\u00d0\7\61\2\2\u00cf\u00d1\5$\23\2\u00d0\u00cf\3"+
		"\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00f1\5*\26\r\u00d3"+
		"\u00d5\7\62\2\2\u00d4\u00d6\5$\23\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3"+
		"\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00f1\5*\26\f\u00d8\u00da\7\65\2\2\u00d9"+
		"\u00db\5$\23\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2"+
		"\2\2\u00dc\u00f1\5*\26\t\u00dd\u00df\7\66\2\2\u00de\u00e0\5$\23\2\u00df"+
		"\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00f1\5*"+
		"\26\b\u00e2\u00e3\7/\2\2\u00e3\u00e4\7\7\2\2\u00e4\u00e5\5*\26\2\u00e5"+
		"\u00e6\7\b\2\2\u00e6\u00f1\3\2\2\2\u00e7\u00e8\7\60\2\2\u00e8\u00e9\7"+
		"\7\2\2\u00e9\u00ea\5*\26\2\u00ea\u00eb\7\b\2\2\u00eb\u00f1\3\2\2\2\u00ec"+
		"\u00ed\79\2\2\u00ed\u00f1\5*\26\4\u00ee\u00ef\78\2\2\u00ef\u00f1\5*\26"+
		"\3\u00f0\u00c6\3\2\2\2\u00f0\u00c8\3\2\2\2\u00f0\u00cc\3\2\2\2\u00f0\u00ce"+
		"\3\2\2\2\u00f0\u00d3\3\2\2\2\u00f0\u00d8\3\2\2\2\u00f0\u00dd\3\2\2\2\u00f0"+
		"\u00e2\3\2\2\2\u00f0\u00e7\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f0\u00ee\3\2"+
		"\2\2\u00f1\u0119\3\2\2\2\u00f2\u00f3\f\25\2\2\u00f3\u00f4\5\36\20\2\u00f4"+
		"\u00f5\5*\26\26\u00f5\u0118\3\2\2\2\u00f6\u00f7\f\22\2\2\u00f7\u00f8\7"+
		"*\2\2\u00f8\u0118\5*\26\23\u00f9\u00fa\f\21\2\2\u00fa\u00fb\7+\2\2\u00fb"+
		"\u0118\5*\26\22\u00fc\u00fd\f\20\2\2\u00fd\u00fe\7-\2\2\u00fe\u0118\5"+
		"*\26\21\u00ff\u0100\f\17\2\2\u0100\u0101\7,\2\2\u0101\u0118\5*\26\20\u0102"+
		"\u0103\f\16\2\2\u0103\u0104\7.\2\2\u0104\u0118\5*\26\17\u0105\u0106\f"+
		"\13\2\2\u0106\u0108\7\63\2\2\u0107\u0109\5$\23\2\u0108\u0107\3\2\2\2\u0108"+
		"\u0109\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0118\5*\26\f\u010b\u010c\f\n"+
		"\2\2\u010c\u010e\7\64\2\2\u010d\u010f\5$\23\2\u010e\u010d\3\2\2\2\u010e"+
		"\u010f\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0118\5*\26\13\u0111\u0112\f"+
		"\7\2\2\u0112\u0114\7\67\2\2\u0113\u0115\5$\23\2\u0114\u0113\3\2\2\2\u0114"+
		"\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\5*\26\b\u0117\u00f2\3\2"+
		"\2\2\u0117\u00f6\3\2\2\2\u0117\u00f9\3\2\2\2\u0117\u00fc\3\2\2\2\u0117"+
		"\u00ff\3\2\2\2\u0117\u0102\3\2\2\2\u0117\u0105\3\2\2\2\u0117\u010b\3\2"+
		"\2\2\u0117\u0111\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119"+
		"\u011a\3\2\2\2\u011a+\3\2\2\2\u011b\u0119\3\2\2\2\36\60\65:<BNTafr\u0091"+
		"\u009f\u00a1\u00aa\u00b0\u00bc\u00c0\u00c2\u00d0\u00d5\u00da\u00df\u00f0"+
		"\u0108\u010e\u0114\u0117\u0119";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}