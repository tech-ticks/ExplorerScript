
// Generated from SsbScript.g4 by ANTLR 4.13.0


#include "SsbScriptLexer.h"


using namespace antlr4;



using namespace antlr4;

namespace {

struct SsbScriptLexerStaticData final {
  SsbScriptLexerStaticData(std::vector<std::string> ruleNames,
                          std::vector<std::string> channelNames,
                          std::vector<std::string> modeNames,
                          std::vector<std::string> literalNames,
                          std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), channelNames(std::move(channelNames)),
        modeNames(std::move(modeNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SsbScriptLexerStaticData(const SsbScriptLexerStaticData&) = delete;
  SsbScriptLexerStaticData(SsbScriptLexerStaticData&&) = delete;
  SsbScriptLexerStaticData& operator=(const SsbScriptLexerStaticData&) = delete;
  SsbScriptLexerStaticData& operator=(SsbScriptLexerStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> channelNames;
  const std::vector<std::string> modeNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag ssbscriptlexerLexerOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
SsbScriptLexerStaticData *ssbscriptlexerLexerStaticData = nullptr;

void ssbscriptlexerLexerInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (ssbscriptlexerLexerStaticData != nullptr) {
    return;
  }
#else
  assert(ssbscriptlexerLexerStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SsbScriptLexerStaticData>(
    std::vector<std::string>{
      "T__0", "STRING_LITERAL", "MULTILINE_STRING_LITERAL", "FOR_TARGET", 
      "CORO", "DEF", "FOR_ACTOR", "FOR_OBJECT", "FOR_PERFORMER", "ALIAS", 
      "FOR", "PREVIOUS", "POSITION", "IDENTIFIER", "VARIABLE", "MACRO_CALL", 
      "INTEGER", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
      "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "ASSIGN", "PLUS", "AT", 
      "PARAGRAPH", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_SHARP", "CLOSE_SHARP", 
      "DECIMAL", "SKIP_", "UNKNOWN_CHAR", "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", 
      "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "SPACES", "LINE_JOINING", 
      "BLOCK_COMMENT", "LINE_COMMENT", "IDENTIFIER_BASE"
    },
    std::vector<std::string>{
      "DEFAULT_TOKEN_CHANNEL", "HIDDEN"
    },
    std::vector<std::string>{
      "DEFAULT_MODE"
    },
    std::vector<std::string>{
      "", "';'", "", "", "", "'coro'", "'def'", "'for_actor'", "'for_object'", 
      "'for_performer'", "'alias'", "'for'", "'previous'", "'Position'", 
      "", "", "", "", "", "", "", "", "'('", "')'", "','", "':'", "'='", 
      "'+'", "'@'", "'\\u00A7'", "'{'", "'}'", "'<'", "'>'"
    },
    std::vector<std::string>{
      "", "", "STRING_LITERAL", "MULTILINE_STRING_LITERAL", "FOR_TARGET", 
      "CORO", "DEF", "FOR_ACTOR", "FOR_OBJECT", "FOR_PERFORMER", "ALIAS", 
      "FOR", "PREVIOUS", "POSITION", "IDENTIFIER", "VARIABLE", "MACRO_CALL", 
      "INTEGER", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
      "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "ASSIGN", "PLUS", "AT", 
      "PARAGRAPH", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_SHARP", "CLOSE_SHARP", 
      "DECIMAL", "SKIP_", "UNKNOWN_CHAR"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,0,36,404,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
  	6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,
  	7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,
  	7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,
  	7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,
  	7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,
  	7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,1,0,1,0,1,1,1,1,1,1,5,1,
  	101,8,1,10,1,12,1,104,9,1,1,1,1,1,1,1,1,1,5,1,110,8,1,10,1,12,1,113,9,
  	1,1,1,3,1,116,8,1,1,2,1,2,1,2,1,2,1,2,5,2,123,8,2,10,2,12,2,126,9,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,136,8,2,10,2,12,2,139,9,2,1,2,1,2,1,
  	2,3,2,144,8,2,1,3,1,3,1,3,3,3,149,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
  	1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
  	1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
  	11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
  	13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,235,8,
  	16,1,17,3,17,238,8,17,1,17,1,17,5,17,242,8,17,10,17,12,17,245,9,17,1,
  	17,3,17,248,8,17,1,17,4,17,251,8,17,11,17,12,17,252,3,17,255,8,17,1,18,
  	3,18,258,8,18,1,18,1,18,1,18,4,18,263,8,18,11,18,12,18,264,1,19,3,19,
  	268,8,19,1,19,1,19,1,19,4,19,273,8,19,11,19,12,19,274,1,20,3,20,278,8,
  	20,1,20,1,20,1,20,4,20,283,8,20,11,20,12,20,284,1,21,1,21,1,22,1,22,1,
  	23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,
  	30,1,30,1,31,1,31,1,32,1,32,1,33,3,33,312,8,33,1,33,4,33,315,8,33,11,
  	33,12,33,316,1,33,1,33,4,33,321,8,33,11,33,12,33,322,1,33,3,33,326,8,
  	33,1,33,1,33,4,33,330,8,33,11,33,12,33,331,3,33,334,8,33,1,34,1,34,1,
  	34,1,34,3,34,340,8,34,1,34,1,34,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,
  	38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,4,42,360,8,42,11,42,12,42,
  	361,1,43,1,43,3,43,366,8,43,1,43,3,43,369,8,43,1,43,1,43,3,43,373,8,43,
  	1,44,1,44,1,44,1,44,5,44,379,8,44,10,44,12,44,382,9,44,1,44,1,44,1,44,
  	3,44,387,8,44,1,45,1,45,1,45,1,45,5,45,393,8,45,10,45,12,45,396,9,45,
  	1,46,1,46,5,46,400,8,46,10,46,12,46,403,9,46,3,124,137,380,0,47,1,1,3,
  	2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
  	31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,
  	27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,0,75,0,77,
  	0,79,0,81,0,83,0,85,0,87,0,89,0,91,0,93,0,1,0,16,4,0,10,10,12,13,39,39,
  	92,92,4,0,10,10,12,13,34,34,92,92,1,0,36,37,1,0,126,126,2,0,79,79,111,
  	111,2,0,88,88,120,120,2,0,66,66,98,98,1,0,49,57,1,0,48,57,1,0,48,55,3,
  	0,48,57,65,70,97,102,1,0,48,49,3,0,9,10,13,13,32,32,2,0,10,10,13,13,3,
  	0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,433,0,1,1,0,0,0,0,3,
  	1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
  	0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,
  	1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
  	0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,
  	0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,
  	1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,
  	0,0,0,69,1,0,0,0,0,71,1,0,0,0,1,95,1,0,0,0,3,115,1,0,0,0,5,143,1,0,0,
  	0,7,148,1,0,0,0,9,150,1,0,0,0,11,155,1,0,0,0,13,159,1,0,0,0,15,169,1,
  	0,0,0,17,180,1,0,0,0,19,194,1,0,0,0,21,200,1,0,0,0,23,204,1,0,0,0,25,
  	213,1,0,0,0,27,222,1,0,0,0,29,224,1,0,0,0,31,227,1,0,0,0,33,234,1,0,0,
  	0,35,254,1,0,0,0,37,257,1,0,0,0,39,267,1,0,0,0,41,277,1,0,0,0,43,286,
  	1,0,0,0,45,288,1,0,0,0,47,290,1,0,0,0,49,292,1,0,0,0,51,294,1,0,0,0,53,
  	296,1,0,0,0,55,298,1,0,0,0,57,300,1,0,0,0,59,302,1,0,0,0,61,304,1,0,0,
  	0,63,306,1,0,0,0,65,308,1,0,0,0,67,333,1,0,0,0,69,339,1,0,0,0,71,343,
  	1,0,0,0,73,345,1,0,0,0,75,348,1,0,0,0,77,350,1,0,0,0,79,352,1,0,0,0,81,
  	354,1,0,0,0,83,356,1,0,0,0,85,359,1,0,0,0,87,363,1,0,0,0,89,374,1,0,0,
  	0,91,388,1,0,0,0,93,397,1,0,0,0,95,96,5,59,0,0,96,2,1,0,0,0,97,102,5,
  	39,0,0,98,101,3,73,36,0,99,101,8,0,0,0,100,98,1,0,0,0,100,99,1,0,0,0,
  	101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,
  	1,0,0,0,105,116,5,39,0,0,106,111,5,34,0,0,107,110,3,73,36,0,108,110,8,
  	1,0,0,109,107,1,0,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,
  	111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,116,5,34,0,0,115,
  	97,1,0,0,0,115,106,1,0,0,0,116,4,1,0,0,0,117,118,5,39,0,0,118,119,5,39,
  	0,0,119,120,5,39,0,0,120,124,1,0,0,0,121,123,9,0,0,0,122,121,1,0,0,0,
  	123,126,1,0,0,0,124,125,1,0,0,0,124,122,1,0,0,0,125,127,1,0,0,0,126,124,
  	1,0,0,0,127,128,5,39,0,0,128,129,5,39,0,0,129,144,5,39,0,0,130,131,5,
  	34,0,0,131,132,5,34,0,0,132,133,5,34,0,0,133,137,1,0,0,0,134,136,9,0,
  	0,0,135,134,1,0,0,0,136,139,1,0,0,0,137,138,1,0,0,0,137,135,1,0,0,0,138,
  	140,1,0,0,0,139,137,1,0,0,0,140,141,5,34,0,0,141,142,5,34,0,0,142,144,
  	5,34,0,0,143,117,1,0,0,0,143,130,1,0,0,0,144,6,1,0,0,0,145,149,3,13,6,
  	0,146,149,3,15,7,0,147,149,3,17,8,0,148,145,1,0,0,0,148,146,1,0,0,0,148,
  	147,1,0,0,0,149,8,1,0,0,0,150,151,5,99,0,0,151,152,5,111,0,0,152,153,
  	5,114,0,0,153,154,5,111,0,0,154,10,1,0,0,0,155,156,5,100,0,0,156,157,
  	5,101,0,0,157,158,5,102,0,0,158,12,1,0,0,0,159,160,5,102,0,0,160,161,
  	5,111,0,0,161,162,5,114,0,0,162,163,5,95,0,0,163,164,5,97,0,0,164,165,
  	5,99,0,0,165,166,5,116,0,0,166,167,5,111,0,0,167,168,5,114,0,0,168,14,
  	1,0,0,0,169,170,5,102,0,0,170,171,5,111,0,0,171,172,5,114,0,0,172,173,
  	5,95,0,0,173,174,5,111,0,0,174,175,5,98,0,0,175,176,5,106,0,0,176,177,
  	5,101,0,0,177,178,5,99,0,0,178,179,5,116,0,0,179,16,1,0,0,0,180,181,5,
  	102,0,0,181,182,5,111,0,0,182,183,5,114,0,0,183,184,5,95,0,0,184,185,
  	5,112,0,0,185,186,5,101,0,0,186,187,5,114,0,0,187,188,5,102,0,0,188,189,
  	5,111,0,0,189,190,5,114,0,0,190,191,5,109,0,0,191,192,5,101,0,0,192,193,
  	5,114,0,0,193,18,1,0,0,0,194,195,5,97,0,0,195,196,5,108,0,0,196,197,5,
  	105,0,0,197,198,5,97,0,0,198,199,5,115,0,0,199,20,1,0,0,0,200,201,5,102,
  	0,0,201,202,5,111,0,0,202,203,5,114,0,0,203,22,1,0,0,0,204,205,5,112,
  	0,0,205,206,5,114,0,0,206,207,5,101,0,0,207,208,5,118,0,0,208,209,5,105,
  	0,0,209,210,5,111,0,0,210,211,5,117,0,0,211,212,5,115,0,0,212,24,1,0,
  	0,0,213,214,5,80,0,0,214,215,5,111,0,0,215,216,5,115,0,0,216,217,5,105,
  	0,0,217,218,5,116,0,0,218,219,5,105,0,0,219,220,5,111,0,0,220,221,5,110,
  	0,0,221,26,1,0,0,0,222,223,3,93,46,0,223,28,1,0,0,0,224,225,7,2,0,0,225,
  	226,3,93,46,0,226,30,1,0,0,0,227,228,7,3,0,0,228,229,3,93,46,0,229,32,
  	1,0,0,0,230,235,3,35,17,0,231,235,3,37,18,0,232,235,3,39,19,0,233,235,
  	3,41,20,0,234,230,1,0,0,0,234,231,1,0,0,0,234,232,1,0,0,0,234,233,1,0,
  	0,0,235,34,1,0,0,0,236,238,5,45,0,0,237,236,1,0,0,0,237,238,1,0,0,0,238,
  	239,1,0,0,0,239,243,3,75,37,0,240,242,3,77,38,0,241,240,1,0,0,0,242,245,
  	1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,255,1,0,0,0,245,243,1,0,0,
  	0,246,248,5,45,0,0,247,246,1,0,0,0,247,248,1,0,0,0,248,250,1,0,0,0,249,
  	251,5,48,0,0,250,249,1,0,0,0,251,252,1,0,0,0,252,250,1,0,0,0,252,253,
  	1,0,0,0,253,255,1,0,0,0,254,237,1,0,0,0,254,247,1,0,0,0,255,36,1,0,0,
  	0,256,258,5,45,0,0,257,256,1,0,0,0,257,258,1,0,0,0,258,259,1,0,0,0,259,
  	260,5,48,0,0,260,262,7,4,0,0,261,263,3,79,39,0,262,261,1,0,0,0,263,264,
  	1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,38,1,0,0,0,266,268,5,45,0,
  	0,267,266,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,270,5,48,0,0,270,
  	272,7,5,0,0,271,273,3,81,40,0,272,271,1,0,0,0,273,274,1,0,0,0,274,272,
  	1,0,0,0,274,275,1,0,0,0,275,40,1,0,0,0,276,278,5,45,0,0,277,276,1,0,0,
  	0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,5,48,0,0,280,282,7,6,0,0,281,
  	283,3,83,41,0,282,281,1,0,0,0,283,284,1,0,0,0,284,282,1,0,0,0,284,285,
  	1,0,0,0,285,42,1,0,0,0,286,287,5,40,0,0,287,44,1,0,0,0,288,289,5,41,0,
  	0,289,46,1,0,0,0,290,291,5,44,0,0,291,48,1,0,0,0,292,293,5,58,0,0,293,
  	50,1,0,0,0,294,295,5,61,0,0,295,52,1,0,0,0,296,297,5,43,0,0,297,54,1,
  	0,0,0,298,299,5,64,0,0,299,56,1,0,0,0,300,301,5,167,0,0,301,58,1,0,0,
  	0,302,303,5,123,0,0,303,60,1,0,0,0,304,305,5,125,0,0,305,62,1,0,0,0,306,
  	307,5,60,0,0,307,64,1,0,0,0,308,309,5,62,0,0,309,66,1,0,0,0,310,312,5,
  	45,0,0,311,310,1,0,0,0,311,312,1,0,0,0,312,314,1,0,0,0,313,315,3,77,38,
  	0,314,313,1,0,0,0,315,316,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,
  	318,1,0,0,0,318,320,5,46,0,0,319,321,3,77,38,0,320,319,1,0,0,0,321,322,
  	1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,334,1,0,0,0,324,326,5,45,
  	0,0,325,324,1,0,0,0,325,326,1,0,0,0,326,327,1,0,0,0,327,329,5,46,0,0,
  	328,330,3,77,38,0,329,328,1,0,0,0,330,331,1,0,0,0,331,329,1,0,0,0,331,
  	332,1,0,0,0,332,334,1,0,0,0,333,311,1,0,0,0,333,325,1,0,0,0,334,68,1,
  	0,0,0,335,340,3,91,45,0,336,340,3,89,44,0,337,340,3,85,42,0,338,340,3,
  	87,43,0,339,335,1,0,0,0,339,336,1,0,0,0,339,337,1,0,0,0,339,338,1,0,0,
  	0,340,341,1,0,0,0,341,342,6,34,0,0,342,70,1,0,0,0,343,344,9,0,0,0,344,
  	72,1,0,0,0,345,346,5,92,0,0,346,347,9,0,0,0,347,74,1,0,0,0,348,349,7,
  	7,0,0,349,76,1,0,0,0,350,351,7,8,0,0,351,78,1,0,0,0,352,353,7,9,0,0,353,
  	80,1,0,0,0,354,355,7,10,0,0,355,82,1,0,0,0,356,357,7,11,0,0,357,84,1,
  	0,0,0,358,360,7,12,0,0,359,358,1,0,0,0,360,361,1,0,0,0,361,359,1,0,0,
  	0,361,362,1,0,0,0,362,86,1,0,0,0,363,365,5,92,0,0,364,366,3,85,42,0,365,
  	364,1,0,0,0,365,366,1,0,0,0,366,372,1,0,0,0,367,369,5,13,0,0,368,367,
  	1,0,0,0,368,369,1,0,0,0,369,370,1,0,0,0,370,373,5,10,0,0,371,373,2,12,
  	13,0,372,368,1,0,0,0,372,371,1,0,0,0,373,88,1,0,0,0,374,375,5,47,0,0,
  	375,376,5,42,0,0,376,380,1,0,0,0,377,379,9,0,0,0,378,377,1,0,0,0,379,
  	382,1,0,0,0,380,381,1,0,0,0,380,378,1,0,0,0,381,386,1,0,0,0,382,380,1,
  	0,0,0,383,384,5,42,0,0,384,387,5,47,0,0,385,387,5,0,0,1,386,383,1,0,0,
  	0,386,385,1,0,0,0,387,90,1,0,0,0,388,389,5,47,0,0,389,390,5,47,0,0,390,
  	394,1,0,0,0,391,393,8,13,0,0,392,391,1,0,0,0,393,396,1,0,0,0,394,392,
  	1,0,0,0,394,395,1,0,0,0,395,92,1,0,0,0,396,394,1,0,0,0,397,401,7,14,0,
  	0,398,400,7,15,0,0,399,398,1,0,0,0,400,403,1,0,0,0,401,399,1,0,0,0,401,
  	402,1,0,0,0,402,94,1,0,0,0,403,401,1,0,0,0,37,0,100,102,109,111,115,124,
  	137,143,148,234,237,243,247,252,254,257,264,267,274,277,284,311,316,322,
  	325,331,333,339,361,365,368,372,380,386,394,401,1,6,0,0
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  ssbscriptlexerLexerStaticData = staticData.release();
}

}

SsbScriptLexer::SsbScriptLexer(CharStream *input) : Lexer(input) {
  SsbScriptLexer::initialize();
  _interpreter = new atn::LexerATNSimulator(this, *ssbscriptlexerLexerStaticData->atn, ssbscriptlexerLexerStaticData->decisionToDFA, ssbscriptlexerLexerStaticData->sharedContextCache);
}

SsbScriptLexer::~SsbScriptLexer() {
  delete _interpreter;
}

std::string SsbScriptLexer::getGrammarFileName() const {
  return "SsbScript.g4";
}

const std::vector<std::string>& SsbScriptLexer::getRuleNames() const {
  return ssbscriptlexerLexerStaticData->ruleNames;
}

const std::vector<std::string>& SsbScriptLexer::getChannelNames() const {
  return ssbscriptlexerLexerStaticData->channelNames;
}

const std::vector<std::string>& SsbScriptLexer::getModeNames() const {
  return ssbscriptlexerLexerStaticData->modeNames;
}

const dfa::Vocabulary& SsbScriptLexer::getVocabulary() const {
  return ssbscriptlexerLexerStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SsbScriptLexer::getSerializedATN() const {
  return ssbscriptlexerLexerStaticData->serializedATN;
}

const atn::ATN& SsbScriptLexer::getATN() const {
  return *ssbscriptlexerLexerStaticData->atn;
}




void SsbScriptLexer::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  ssbscriptlexerLexerInitialize();
#else
  ::antlr4::internal::call_once(ssbscriptlexerLexerOnceFlag, ssbscriptlexerLexerInitialize);
#endif
}