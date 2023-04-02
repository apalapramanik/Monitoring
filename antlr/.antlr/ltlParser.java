// Generated from /home/apramani/STL RESEARCH/monitoring/antlr/ltlParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ltlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MINUS=1, PLUS=2, TIMES=3, DIVIDE=4, LPAREN=5, RPAREN=6, LBRACE=7, RBRACE=8, 
		LBRACK=9, RBRACK=10, SEMICOLON=11, COLON=12, COMMA=13, DOT=14, AT=15, 
		ABS=16, SQRT=17, EXP=18, POW=19, SEC=20, MSEC=21, USEC=22, NSEC=23, PSEC=24, 
		ROS_Topic=25, Import=26, Input=27, Output=28, Internal=29, Constant=30, 
		DomainTypeReal=31, DomainTypeFloat=32, DomainTypeLong=33, DomainTypeComplex=34, 
		DomainTypeInt=35, DomainTypeBool=36, Assertion=37, Specification=38, From=39, 
		NotOperator=40, OrOperator=41, AndOperator=42, IffOperator=43, ImpliesOperator=44, 
		XorOperator=45, RiseOperator=46, FallOperator=47, AlwaysOperator=48, EventuallyOperator=49, 
		UntilOperator=50, UnlessOperator=51, HistoricallyOperator=52, OnceOperator=53, 
		SinceOperator=54, NextOperator=55, PreviousOperator=56, EqualOperator=57, 
		NotEqualOperator=58, GreaterOrEqualOperator=59, LesserOrEqualOperator=60, 
		GreaterOperator=61, LesserOperator=62, EQUAL=63, BooleanLiteral=64, TRUE=65, 
		FALSE=66, IntegerLiteral=67, RealLiteral=68, Identifier=69, LINE_TERMINATOR=70, 
		WHITESPACE=71, COMMENT=72, LINE_COMMENT=73;
	public static final int
		RULE_specification_file = 0, RULE_specification = 1, RULE_spec = 2, RULE_modimport = 3, 
		RULE_assertion = 4, RULE_declaration = 5, RULE_annotation = 6, RULE_annotation_type = 7, 
		RULE_variableDeclaration = 8, RULE_constantDeclaration = 9, RULE_assignment = 10, 
		RULE_domainType = 11, RULE_ioType = 12, RULE_expression = 13, RULE_real_expression = 14, 
		RULE_comparisonOp = 15, RULE_literal = 16, RULE_identifier = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"specification_file", "specification", "spec", "modimport", "assertion", 
			"declaration", "annotation", "annotation_type", "variableDeclaration", 
			"constantDeclaration", "assignment", "domainType", "ioType", "expression", 
			"real_expression", "comparisonOp", "literal", "identifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'-'", "'+'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
			"']'", "';'", "':'", "','", "'.'", "'@'", "'abs'", "'sqrt'", "'exp'", 
			"'pow'", "'s'", "'ms'", "'us'", "'ns'", "'ps'", "'topic'", "'import'", 
			"'input'", "'output'", "'internal'", "'const'", "'real'", "'float'", 
			"'long'", "'complex'", "'int'", "'bool'", "'assertion'", "'specification'", 
			"'from'", null, null, null, null, null, "'xor'", "'rise'", "'fall'", 
			null, null, null, null, null, null, null, null, null, "'=='", "'!=='", 
			"'>='", "'<='", "'>'", "'<'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MINUS", "PLUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "LBRACK", "RBRACK", "SEMICOLON", "COLON", "COMMA", "DOT", "AT", 
			"ABS", "SQRT", "EXP", "POW", "SEC", "MSEC", "USEC", "NSEC", "PSEC", "ROS_Topic", 
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
	public String getGrammarFileName() { return "ltlParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ltlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Specification_fileContext extends ParserRuleContext {
		public SpecificationContext specification() {
			return getRuleContext(SpecificationContext.class,0);
		}
		public TerminalNode EOF() { return getToken(ltlParser.EOF, 0); }
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
			setState(36);
			specification();
			setState(37);
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
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Specification) {
				{
				setState(39);
				spec();
				}
			}

			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==From) {
				{
				{
				setState(42);
				modimport();
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(50);
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
						setState(48);
						declaration();
						}
						break;
					case AT:
						{
						setState(49);
						annotation();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(54);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(56); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(55);
				assertion();
				}
				}
				setState(58); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MINUS) | (1L << LPAREN) | (1L << ABS) | (1L << SQRT) | (1L << EXP) | (1L << POW) | (1L << NotOperator) | (1L << RiseOperator) | (1L << FallOperator) | (1L << AlwaysOperator) | (1L << EventuallyOperator) | (1L << HistoricallyOperator) | (1L << OnceOperator) | (1L << NextOperator) | (1L << PreviousOperator))) != 0) || ((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & ((1L << (IntegerLiteral - 67)) | (1L << (RealLiteral - 67)) | (1L << (Identifier - 67)))) != 0) );
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
		public TerminalNode Specification() { return getToken(ltlParser.Specification, 0); }
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
		public SpecificationIdContext(SpecContext ctx) { copyFrom(ctx); }
	}

	public final SpecContext spec() throws RecognitionException {
		SpecContext _localctx = new SpecContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_spec);
		try {
			_localctx = new SpecificationIdContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(Specification);
			setState(61);
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
		public TerminalNode From() { return getToken(ltlParser.From, 0); }
		public List<TerminalNode> Identifier() { return getTokens(ltlParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(ltlParser.Identifier, i);
		}
		public TerminalNode Import() { return getToken(ltlParser.Import, 0); }
		public ModImportContext(ModimportContext ctx) { copyFrom(ctx); }
	}

	public final ModimportContext modimport() throws RecognitionException {
		ModimportContext _localctx = new ModimportContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_modimport);
		try {
			_localctx = new ModImportContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(From);
			setState(64);
			match(Identifier);
			setState(65);
			match(Import);
			setState(66);
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
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
		public TerminalNode EQUAL() { return getToken(ltlParser.EQUAL, 0); }
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
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(68);
				match(Identifier);
				setState(69);
				match(EQUAL);
				}
				break;
			}
			setState(72);
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
			setState(76);
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
				setState(74);
				variableDeclaration();
				}
				break;
			case Constant:
				_localctx = new DeclConstantContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
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
		public TerminalNode AT() { return getToken(ltlParser.AT, 0); }
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
			setState(78);
			match(AT);
			setState(79);
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
		public TerminalNode ROS_Topic() { return getToken(ltlParser.ROS_Topic, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public List<TerminalNode> Identifier() { return getTokens(ltlParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(ltlParser.Identifier, i);
		}
		public TerminalNode COMMA() { return getToken(ltlParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public RosTopicContext(Annotation_typeContext ctx) { copyFrom(ctx); }
	}

	public final Annotation_typeContext annotation_type() throws RecognitionException {
		Annotation_typeContext _localctx = new Annotation_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_annotation_type);
		try {
			_localctx = new RosTopicContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(ROS_Topic);
			setState(82);
			match(LPAREN);
			setState(83);
			match(Identifier);
			setState(84);
			match(COMMA);
			setState(85);
			match(Identifier);
			setState(86);
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
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
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
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Input || _la==Output) {
				{
				setState(88);
				ioType();
				}
			}

			setState(91);
			domainType();
			setState(92);
			match(Identifier);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(93);
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
		public TerminalNode Constant() { return getToken(ltlParser.Constant, 0); }
		public DomainTypeContext domainType() {
			return getRuleContext(DomainTypeContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
		public TerminalNode EQUAL() { return getToken(ltlParser.EQUAL, 0); }
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
			setState(96);
			match(Constant);
			setState(97);
			domainType();
			setState(98);
			match(Identifier);
			setState(99);
			match(EQUAL);
			setState(100);
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
		public TerminalNode EQUAL() { return getToken(ltlParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AsgnExprContext(AssignmentContext ctx) { copyFrom(ctx); }
	}
	public static class AsgnLiteralContext extends AssignmentContext {
		public TerminalNode EQUAL() { return getToken(ltlParser.EQUAL, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public AsgnLiteralContext(AssignmentContext ctx) { copyFrom(ctx); }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assignment);
		try {
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				_localctx = new AsgnLiteralContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				match(EQUAL);
				setState(103);
				literal();
				}
				break;
			case 2:
				_localctx = new AsgnExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				match(EQUAL);
				setState(105);
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
		public TerminalNode DomainTypeFloat() { return getToken(ltlParser.DomainTypeFloat, 0); }
		public TerminalNode DomainTypeInt() { return getToken(ltlParser.DomainTypeInt, 0); }
		public TerminalNode DomainTypeLong() { return getToken(ltlParser.DomainTypeLong, 0); }
		public TerminalNode DomainTypeComplex() { return getToken(ltlParser.DomainTypeComplex, 0); }
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
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
			setState(108);
			_la = _input.LA(1);
			if ( !(((((_la - 32)) & ~0x3f) == 0 && ((1L << (_la - 32)) & ((1L << (DomainTypeFloat - 32)) | (1L << (DomainTypeLong - 32)) | (1L << (DomainTypeComplex - 32)) | (1L << (DomainTypeInt - 32)) | (1L << (Identifier - 32)))) != 0)) ) {
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
		public TerminalNode Input() { return getToken(ltlParser.Input, 0); }
		public TerminalNode Output() { return getToken(ltlParser.Output, 0); }
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
			setState(110);
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
		public TerminalNode SinceOperator() { return getToken(ltlParser.SinceOperator, 0); }
		public ExprSinceContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprParenContext extends ExpressionContext {
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public ExprParenContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprIffContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode IffOperator() { return getToken(ltlParser.IffOperator, 0); }
		public ExprIffContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExpreOnceContext extends ExpressionContext {
		public TerminalNode OnceOperator() { return getToken(ltlParser.OnceOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpreOnceContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprEvContext extends ExpressionContext {
		public TerminalNode EventuallyOperator() { return getToken(ltlParser.EventuallyOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
		public TerminalNode ImpliesOperator() { return getToken(ltlParser.ImpliesOperator, 0); }
		public ExprImpliesContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprUntilContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode UntilOperator() { return getToken(ltlParser.UntilOperator, 0); }
		public ExprUntilContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprNotContext extends ExpressionContext {
		public TerminalNode NotOperator() { return getToken(ltlParser.NotOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprNotContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprNextContext extends ExpressionContext {
		public TerminalNode NextOperator() { return getToken(ltlParser.NextOperator, 0); }
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
		public TerminalNode AndOperator() { return getToken(ltlParser.AndOperator, 0); }
		public ExprAndContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprUnlessContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode UnlessOperator() { return getToken(ltlParser.UnlessOperator, 0); }
		public ExprUnlessContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprPreviousContext extends ExpressionContext {
		public TerminalNode PreviousOperator() { return getToken(ltlParser.PreviousOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprPreviousContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprHistContext extends ExpressionContext {
		public TerminalNode HistoricallyOperator() { return getToken(ltlParser.HistoricallyOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprHistContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprFallContext extends ExpressionContext {
		public TerminalNode FallOperator() { return getToken(ltlParser.FallOperator, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
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
		public TerminalNode XorOperator() { return getToken(ltlParser.XorOperator, 0); }
		public ExprXorContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprRiseContext extends ExpressionContext {
		public TerminalNode RiseOperator() { return getToken(ltlParser.RiseOperator, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public ExprRiseContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprOrContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OrOperator() { return getToken(ltlParser.OrOperator, 0); }
		public ExprOrContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAlwaysContext extends ExpressionContext {
		public TerminalNode AlwaysOperator() { return getToken(ltlParser.AlwaysOperator, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
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

				setState(113);
				real_expression(0);
				}
				break;
			case LPAREN:
				{
				_localctx = new ExprParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(114);
				match(LPAREN);
				setState(115);
				expression(0);
				setState(116);
				match(RPAREN);
				}
				break;
			case NotOperator:
				{
				_localctx = new ExprNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(118);
				match(NotOperator);
				setState(119);
				expression(17);
				}
				break;
			case AlwaysOperator:
				{
				_localctx = new ExprAlwaysContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(120);
				match(AlwaysOperator);
				setState(121);
				expression(11);
				}
				break;
			case EventuallyOperator:
				{
				_localctx = new ExprEvContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(122);
				match(EventuallyOperator);
				setState(123);
				expression(10);
				}
				break;
			case HistoricallyOperator:
				{
				_localctx = new ExprHistContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				match(HistoricallyOperator);
				setState(125);
				expression(7);
				}
				break;
			case OnceOperator:
				{
				_localctx = new ExpreOnceContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(126);
				match(OnceOperator);
				setState(127);
				expression(6);
				}
				break;
			case RiseOperator:
				{
				_localctx = new ExprRiseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(128);
				match(RiseOperator);
				setState(129);
				match(LPAREN);
				setState(130);
				expression(0);
				setState(131);
				match(RPAREN);
				}
				break;
			case FallOperator:
				{
				_localctx = new ExprFallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(133);
				match(FallOperator);
				setState(134);
				match(LPAREN);
				setState(135);
				expression(0);
				setState(136);
				match(RPAREN);
				}
				break;
			case PreviousOperator:
				{
				_localctx = new ExprPreviousContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(138);
				match(PreviousOperator);
				setState(139);
				expression(2);
				}
				break;
			case NextOperator:
				{
				_localctx = new ExprNextContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(140);
				match(NextOperator);
				setState(141);
				expression(1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(174);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(172);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new ExprPredicateContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(144);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(145);
						comparisonOp();
						setState(146);
						expression(20);
						}
						break;
					case 2:
						{
						_localctx = new ExprOrContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(148);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(149);
						match(OrOperator);
						setState(150);
						expression(17);
						}
						break;
					case 3:
						{
						_localctx = new ExprAndContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(151);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(152);
						match(AndOperator);
						setState(153);
						expression(16);
						}
						break;
					case 4:
						{
						_localctx = new ExprImpliesContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(154);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(155);
						match(ImpliesOperator);
						setState(156);
						expression(15);
						}
						break;
					case 5:
						{
						_localctx = new ExprIffContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(157);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(158);
						match(IffOperator);
						setState(159);
						expression(14);
						}
						break;
					case 6:
						{
						_localctx = new ExprXorContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(160);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(161);
						match(XorOperator);
						setState(162);
						expression(13);
						}
						break;
					case 7:
						{
						_localctx = new ExprUntilContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(163);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(164);
						match(UntilOperator);
						setState(165);
						expression(10);
						}
						break;
					case 8:
						{
						_localctx = new ExprUnlessContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(166);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(167);
						match(UnlessOperator);
						setState(168);
						expression(9);
						}
						break;
					case 9:
						{
						_localctx = new ExprSinceContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(169);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(170);
						match(SinceOperator);
						setState(171);
						expression(6);
						}
						break;
					}
					} 
				}
				setState(176);
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
		public TerminalNode MINUS() { return getToken(ltlParser.MINUS, 0); }
		public ExprSubtractionContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprPowContext extends Real_expressionContext {
		public TerminalNode POW() { return getToken(ltlParser.POW, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(ltlParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public ExprPowContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprDivisionContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode DIVIDE() { return getToken(ltlParser.DIVIDE, 0); }
		public ExprDivisionContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprMultiplicationContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode TIMES() { return getToken(ltlParser.TIMES, 0); }
		public ExprMultiplicationContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprLiteralContext extends Real_expressionContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ExprLiteralContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprExpContext extends Real_expressionContext {
		public TerminalNode EXP() { return getToken(ltlParser.EXP, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public ExprExpContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprSqrtContext extends Real_expressionContext {
		public TerminalNode SQRT() { return getToken(ltlParser.SQRT, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public ExprSqrtContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprIdContext extends Real_expressionContext {
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
		public ExprIdContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAbsContext extends Real_expressionContext {
		public TerminalNode ABS() { return getToken(ltlParser.ABS, 0); }
		public TerminalNode LPAREN() { return getToken(ltlParser.LPAREN, 0); }
		public Real_expressionContext real_expression() {
			return getRuleContext(Real_expressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ltlParser.RPAREN, 0); }
		public ExprAbsContext(Real_expressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExprAdditionContext extends Real_expressionContext {
		public List<Real_expressionContext> real_expression() {
			return getRuleContexts(Real_expressionContext.class);
		}
		public Real_expressionContext real_expression(int i) {
			return getRuleContext(Real_expressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(ltlParser.PLUS, 0); }
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
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_real_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Identifier:
				{
				_localctx = new ExprIdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(178);
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
				setState(179);
				literal();
				}
				break;
			case ABS:
				{
				_localctx = new ExprAbsContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(180);
				match(ABS);
				setState(181);
				match(LPAREN);
				setState(182);
				real_expression(0);
				setState(183);
				match(RPAREN);
				}
				break;
			case SQRT:
				{
				_localctx = new ExprSqrtContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(185);
				match(SQRT);
				setState(186);
				match(LPAREN);
				setState(187);
				real_expression(0);
				setState(188);
				match(RPAREN);
				}
				break;
			case EXP:
				{
				_localctx = new ExprExpContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(190);
				match(EXP);
				setState(191);
				match(LPAREN);
				setState(192);
				real_expression(0);
				setState(193);
				match(RPAREN);
				}
				break;
			case POW:
				{
				_localctx = new ExprPowContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(195);
				match(POW);
				setState(196);
				match(LPAREN);
				setState(197);
				real_expression(0);
				setState(198);
				match(COMMA);
				setState(199);
				real_expression(0);
				setState(200);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(218);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(216);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new ExprAdditionContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(204);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(205);
						match(PLUS);
						setState(206);
						real_expression(9);
						}
						break;
					case 2:
						{
						_localctx = new ExprSubtractionContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(207);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(208);
						match(MINUS);
						setState(209);
						real_expression(8);
						}
						break;
					case 3:
						{
						_localctx = new ExprMultiplicationContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(210);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(211);
						match(TIMES);
						setState(212);
						real_expression(7);
						}
						break;
					case 4:
						{
						_localctx = new ExprDivisionContext(new Real_expressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_real_expression);
						setState(213);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(214);
						match(DIVIDE);
						setState(215);
						real_expression(6);
						}
						break;
					}
					} 
				}
				setState(220);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
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
		public TerminalNode GreaterOrEqualOperator() { return getToken(ltlParser.GreaterOrEqualOperator, 0); }
		public GeqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class LeqContext extends ComparisonOpContext {
		public TerminalNode LesserOrEqualOperator() { return getToken(ltlParser.LesserOrEqualOperator, 0); }
		public LeqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterContext extends ComparisonOpContext {
		public TerminalNode GreaterOperator() { return getToken(ltlParser.GreaterOperator, 0); }
		public GreaterContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class NeqContext extends ComparisonOpContext {
		public TerminalNode NotEqualOperator() { return getToken(ltlParser.NotEqualOperator, 0); }
		public NeqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class EqContext extends ComparisonOpContext {
		public TerminalNode EqualOperator() { return getToken(ltlParser.EqualOperator, 0); }
		public EqContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}
	public static class LessContext extends ComparisonOpContext {
		public TerminalNode LesserOperator() { return getToken(ltlParser.LesserOperator, 0); }
		public LessContext(ComparisonOpContext ctx) { copyFrom(ctx); }
	}

	public final ComparisonOpContext comparisonOp() throws RecognitionException {
		ComparisonOpContext _localctx = new ComparisonOpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_comparisonOp);
		try {
			setState(227);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LesserOrEqualOperator:
				_localctx = new LeqContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				match(LesserOrEqualOperator);
				}
				break;
			case GreaterOrEqualOperator:
				_localctx = new GeqContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(222);
				match(GreaterOrEqualOperator);
				}
				break;
			case LesserOperator:
				_localctx = new LessContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(223);
				match(LesserOperator);
				}
				break;
			case GreaterOperator:
				_localctx = new GreaterContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(224);
				match(GreaterOperator);
				}
				break;
			case EqualOperator:
				_localctx = new EqContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(225);
				match(EqualOperator);
				}
				break;
			case NotEqualOperator:
				_localctx = new NeqContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(226);
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
		public TerminalNode IntegerLiteral() { return getToken(ltlParser.IntegerLiteral, 0); }
		public TerminalNode RealLiteral() { return getToken(ltlParser.RealLiteral, 0); }
		public TerminalNode MINUS() { return getToken(ltlParser.MINUS, 0); }
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
		enterRule(_localctx, 32, RULE_literal);
		try {
			setState(233);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IntegerLiteral:
				enterOuterAlt(_localctx, 1);
				{
				setState(229);
				match(IntegerLiteral);
				}
				break;
			case RealLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(230);
				match(RealLiteral);
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(231);
				match(MINUS);
				setState(232);
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
		public TerminalNode Identifier() { return getToken(ltlParser.Identifier, 0); }
		public IdContext(IdentifierContext ctx) { copyFrom(ctx); }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_identifier);
		try {
			_localctx = new IdContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 14:
			return real_expression_sempred((Real_expressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 19);
		case 1:
			return precpred(_ctx, 16);
		case 2:
			return precpred(_ctx, 15);
		case 3:
			return precpred(_ctx, 14);
		case 4:
			return precpred(_ctx, 13);
		case 5:
			return precpred(_ctx, 12);
		case 6:
			return precpred(_ctx, 9);
		case 7:
			return precpred(_ctx, 8);
		case 8:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean real_expression_sempred(Real_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 9:
			return precpred(_ctx, 8);
		case 10:
			return precpred(_ctx, 7);
		case 11:
			return precpred(_ctx, 6);
		case 12:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K\u00f0\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\3\3\5\3+\n\3\3\3\7\3.\n\3\f\3\16\3\61\13\3\3\3"+
		"\3\3\7\3\65\n\3\f\3\16\38\13\3\3\3\6\3;\n\3\r\3\16\3<\3\4\3\4\3\4\3\5"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\5\6I\n\6\3\6\3\6\3\7\3\7\5\7O\n\7\3\b\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\5\n\\\n\n\3\n\3\n\3\n\5\na\n\n\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\fm\n\f\3\r\3\r\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\5\17\u0091\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\7\17\u00af\n\17\f\17\16\17\u00b2\13\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00cd\n\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00db\n\20\f\20"+
		"\16\20\u00de\13\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00e6\n\21\3\22"+
		"\3\22\3\22\3\22\5\22\u00ec\n\22\3\23\3\23\3\23\2\4\34\36\24\2\4\6\b\n"+
		"\f\16\20\22\24\26\30\32\34\36 \"$\2\4\4\2\"%GG\3\2\35\36\2\u010a\2&\3"+
		"\2\2\2\4*\3\2\2\2\6>\3\2\2\2\bA\3\2\2\2\nH\3\2\2\2\fN\3\2\2\2\16P\3\2"+
		"\2\2\20S\3\2\2\2\22[\3\2\2\2\24b\3\2\2\2\26l\3\2\2\2\30n\3\2\2\2\32p\3"+
		"\2\2\2\34\u0090\3\2\2\2\36\u00cc\3\2\2\2 \u00e5\3\2\2\2\"\u00eb\3\2\2"+
		"\2$\u00ed\3\2\2\2&\'\5\4\3\2\'(\7\2\2\3(\3\3\2\2\2)+\5\6\4\2*)\3\2\2\2"+
		"*+\3\2\2\2+/\3\2\2\2,.\5\b\5\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2"+
		"\2\2\60\66\3\2\2\2\61/\3\2\2\2\62\65\5\f\7\2\63\65\5\16\b\2\64\62\3\2"+
		"\2\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67:\3\2\2\2"+
		"8\66\3\2\2\29;\5\n\6\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\5\3\2"+
		"\2\2>?\7(\2\2?@\7G\2\2@\7\3\2\2\2AB\7)\2\2BC\7G\2\2CD\7\34\2\2DE\7G\2"+
		"\2E\t\3\2\2\2FG\7G\2\2GI\7A\2\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\5\34\17"+
		"\2K\13\3\2\2\2LO\5\22\n\2MO\5\24\13\2NL\3\2\2\2NM\3\2\2\2O\r\3\2\2\2P"+
		"Q\7\21\2\2QR\5\20\t\2R\17\3\2\2\2ST\7\33\2\2TU\7\7\2\2UV\7G\2\2VW\7\17"+
		"\2\2WX\7G\2\2XY\7\b\2\2Y\21\3\2\2\2Z\\\5\32\16\2[Z\3\2\2\2[\\\3\2\2\2"+
		"\\]\3\2\2\2]^\5\30\r\2^`\7G\2\2_a\5\26\f\2`_\3\2\2\2`a\3\2\2\2a\23\3\2"+
		"\2\2bc\7 \2\2cd\5\30\r\2de\7G\2\2ef\7A\2\2fg\5\"\22\2g\25\3\2\2\2hi\7"+
		"A\2\2im\5\"\22\2jk\7A\2\2km\5\34\17\2lh\3\2\2\2lj\3\2\2\2m\27\3\2\2\2"+
		"no\t\2\2\2o\31\3\2\2\2pq\t\3\2\2q\33\3\2\2\2rs\b\17\1\2s\u0091\5\36\20"+
		"\2tu\7\7\2\2uv\5\34\17\2vw\7\b\2\2w\u0091\3\2\2\2xy\7*\2\2y\u0091\5\34"+
		"\17\23z{\7\62\2\2{\u0091\5\34\17\r|}\7\63\2\2}\u0091\5\34\17\f~\177\7"+
		"\66\2\2\177\u0091\5\34\17\t\u0080\u0081\7\67\2\2\u0081\u0091\5\34\17\b"+
		"\u0082\u0083\7\60\2\2\u0083\u0084\7\7\2\2\u0084\u0085\5\34\17\2\u0085"+
		"\u0086\7\b\2\2\u0086\u0091\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7"+
		"\7\2\2\u0089\u008a\5\34\17\2\u008a\u008b\7\b\2\2\u008b\u0091\3\2\2\2\u008c"+
		"\u008d\7:\2\2\u008d\u0091\5\34\17\4\u008e\u008f\79\2\2\u008f\u0091\5\34"+
		"\17\3\u0090r\3\2\2\2\u0090t\3\2\2\2\u0090x\3\2\2\2\u0090z\3\2\2\2\u0090"+
		"|\3\2\2\2\u0090~\3\2\2\2\u0090\u0080\3\2\2\2\u0090\u0082\3\2\2\2\u0090"+
		"\u0087\3\2\2\2\u0090\u008c\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u00b0\3\2"+
		"\2\2\u0092\u0093\f\25\2\2\u0093\u0094\5 \21\2\u0094\u0095\5\34\17\26\u0095"+
		"\u00af\3\2\2\2\u0096\u0097\f\22\2\2\u0097\u0098\7+\2\2\u0098\u00af\5\34"+
		"\17\23\u0099\u009a\f\21\2\2\u009a\u009b\7,\2\2\u009b\u00af\5\34\17\22"+
		"\u009c\u009d\f\20\2\2\u009d\u009e\7.\2\2\u009e\u00af\5\34\17\21\u009f"+
		"\u00a0\f\17\2\2\u00a0\u00a1\7-\2\2\u00a1\u00af\5\34\17\20\u00a2\u00a3"+
		"\f\16\2\2\u00a3\u00a4\7/\2\2\u00a4\u00af\5\34\17\17\u00a5\u00a6\f\13\2"+
		"\2\u00a6\u00a7\7\64\2\2\u00a7\u00af\5\34\17\f\u00a8\u00a9\f\n\2\2\u00a9"+
		"\u00aa\7\65\2\2\u00aa\u00af\5\34\17\13\u00ab\u00ac\f\7\2\2\u00ac\u00ad"+
		"\78\2\2\u00ad\u00af\5\34\17\b\u00ae\u0092\3\2\2\2\u00ae\u0096\3\2\2\2"+
		"\u00ae\u0099\3\2\2\2\u00ae\u009c\3\2\2\2\u00ae\u009f\3\2\2\2\u00ae\u00a2"+
		"\3\2\2\2\u00ae\u00a5\3\2\2\2\u00ae\u00a8\3\2\2\2\u00ae\u00ab\3\2\2\2\u00af"+
		"\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\35\3\2\2"+
		"\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\b\20\1\2\u00b4\u00cd\7G\2\2\u00b5\u00cd"+
		"\5\"\22\2\u00b6\u00b7\7\22\2\2\u00b7\u00b8\7\7\2\2\u00b8\u00b9\5\36\20"+
		"\2\u00b9\u00ba\7\b\2\2\u00ba\u00cd\3\2\2\2\u00bb\u00bc\7\23\2\2\u00bc"+
		"\u00bd\7\7\2\2\u00bd\u00be\5\36\20\2\u00be\u00bf\7\b\2\2\u00bf\u00cd\3"+
		"\2\2\2\u00c0\u00c1\7\24\2\2\u00c1\u00c2\7\7\2\2\u00c2\u00c3\5\36\20\2"+
		"\u00c3\u00c4\7\b\2\2\u00c4\u00cd\3\2\2\2\u00c5\u00c6\7\25\2\2\u00c6\u00c7"+
		"\7\7\2\2\u00c7\u00c8\5\36\20\2\u00c8\u00c9\7\17\2\2\u00c9\u00ca\5\36\20"+
		"\2\u00ca\u00cb\7\b\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00b3\3\2\2\2\u00cc\u00b5"+
		"\3\2\2\2\u00cc\u00b6\3\2\2\2\u00cc\u00bb\3\2\2\2\u00cc\u00c0\3\2\2\2\u00cc"+
		"\u00c5\3\2\2\2\u00cd\u00dc\3\2\2\2\u00ce\u00cf\f\n\2\2\u00cf\u00d0\7\4"+
		"\2\2\u00d0\u00db\5\36\20\13\u00d1\u00d2\f\t\2\2\u00d2\u00d3\7\3\2\2\u00d3"+
		"\u00db\5\36\20\n\u00d4\u00d5\f\b\2\2\u00d5\u00d6\7\5\2\2\u00d6\u00db\5"+
		"\36\20\t\u00d7\u00d8\f\7\2\2\u00d8\u00d9\7\6\2\2\u00d9\u00db\5\36\20\b"+
		"\u00da\u00ce\3\2\2\2\u00da\u00d1\3\2\2\2\u00da\u00d4\3\2\2\2\u00da\u00d7"+
		"\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd"+
		"\37\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e6\7>\2\2\u00e0\u00e6\7=\2\2"+
		"\u00e1\u00e6\7@\2\2\u00e2\u00e6\7?\2\2\u00e3\u00e6\7;\2\2\u00e4\u00e6"+
		"\7<\2\2\u00e5\u00df\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5"+
		"\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6!\3\2\2\2"+
		"\u00e7\u00ec\7E\2\2\u00e8\u00ec\7F\2\2\u00e9\u00ea\7\3\2\2\u00ea\u00ec"+
		"\5\"\22\2\u00eb\u00e7\3\2\2\2\u00eb\u00e8\3\2\2\2\u00eb\u00e9\3\2\2\2"+
		"\u00ec#\3\2\2\2\u00ed\u00ee\7G\2\2\u00ee%\3\2\2\2\24*/\64\66<HN[`l\u0090"+
		"\u00ae\u00b0\u00cc\u00da\u00dc\u00e5\u00eb";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}